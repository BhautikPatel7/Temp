import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.regularizers import l2
import tensorflow as tf
import numpy as np

# Database connection setup
DATABASE_TYPE = 'mysql'
DBAPI = 'pymysql'
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'root'
DATABASE = 'pmp_v2_org121'
PORT = 3306

DATABASE_URL = f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = sqlalchemy.create_engine(DATABASE_URL)



DATABASE_TYPE_1 = 'mysql'
DBAPI_1 = 'pymysql'
HOST_1 = '127.0.0.1'
USER_1 = 'root'
PASSWORD_1 = 'root'
DATABASE_1 = 'pmp_v2_org499'
PORT_1 = 3306

DATABASE_URL_1 = f"{DATABASE_TYPE_1}+{DBAPI_1}://{USER_1}:{PASSWORD_1}@{HOST_1}:{PORT_1}/{DATABASE_1}"
engine_1 = sqlalchemy.create_engine(DATABASE_URL_1)

# Query to filter data
ca_report_filtered_df = pd.read_sql("""
SELECT CA_ID, CA_Start, CA_Finish, CA_ActualStart, CA_ActualFinish
FROM ca_report
WHERE CA_ID IN (
    SELECT CA_ID
    FROM ca
    WHERE CA_IsCA0 = 1
)
AND CA_ActualFinish IS NOT NULL;
""", engine)

# Load milestone data
milestones_df_2 = pd.read_sql("""
SELECT Milestone_ID, MS_Plan, MS_BL, MS_Actual, MS_Desc, MS_Name, MS_Color, CA_ID, Pr_ID, BU_ID, Org_ID, MS_Reported, MS_ShowInGantt
FROM milestones
WHERE CA_ID IN (
    SELECT CA_ID
    FROM ca_report
    WHERE CA_ID IN (
        SELECT CA_ID
        FROM ca
        WHERE CA_IsCA0 = 1
    )
    AND CA_ActualFinish IS NOT NULL
) AND MS_Plan IS NOT NULL AND MS_BL IS NOT NULL;
""", engine)


ca_report_filtered_df_2 = pd.read_sql("""
SELECT CA_ID, CA_Start, CA_Finish, CA_ActualStart, CA_ActualFinish
FROM ca_report
WHERE CA_ID IN (
    SELECT CA_ID
    FROM ca
    WHERE CA_IsCA0 = 1
)
AND CA_ActualFinish IS NOT NULL;
""", engine_1)

# Load milestone data
milestones_df_1 = pd.read_sql("""
SELECT Milestone_ID, MS_Plan, MS_BL, MS_Actual, MS_Desc, MS_Name, MS_Color, CA_ID, Pr_ID, BU_ID, Org_ID, MS_Reported, MS_ShowInGantt
FROM milestones
WHERE CA_ID IN (
    SELECT CA_ID
    FROM ca_report
    WHERE CA_ID IN (
        SELECT CA_ID
        FROM ca
        WHERE CA_IsCA0 = 1
    )
    AND CA_ActualFinish IS NOT NULL
) AND MS_Plan IS NOT NULL AND MS_BL IS NOT NULL;
""", engine_1)



# Combine the CA report data from both databases
ca_report_filtered_df_combined = pd.concat([ca_report_filtered_df, ca_report_filtered_df_2], ignore_index=True)

# Combine the milestone data from both databases
milestones_df_combined = pd.concat([milestones_df_1, milestones_df_2], ignore_index=True)

# Convert milestone dates to datetime
milestones_df_combined['MS_Plan'] = pd.to_datetime(milestones_df_combined['MS_Plan'])
milestones_df_combined['MS_BL'] = pd.to_datetime(milestones_df_combined['MS_BL'])
milestones_df_combined['MS_Actual'] = pd.to_datetime(milestones_df_combined['MS_Actual'])

# Feature engineering: calculate deviations
milestones_df_combined['Deviation_From_Plan'] = (milestones_df_combined['MS_Actual'] - milestones_df_combined['MS_Plan']).dt.days
milestones_df_combined['Deviation_From_BL'] = (milestones_df_combined['MS_Actual'] - milestones_df_combined['MS_BL']).dt.days
milestones_df_combined['Reported'] = milestones_df_combined['MS_Reported'].astype(int)
milestones_df_combined['Visible_In_Gantt'] = milestones_df_combined['MS_ShowInGantt'].astype(int)

# Convert date columns to datetime
ca_report_filtered_df_combined['CA_ActualFinish'] = pd.to_datetime(ca_report_filtered_df_combined['CA_ActualFinish'])
ca_report_filtered_df_combined['CA_Start'] = pd.to_datetime(ca_report_filtered_df_combined['CA_Start'])
ca_report_filtered_df_combined.dropna(inplace=True)

# Feature Engineering
ca_report_filtered_df_combined['Duration'] = (ca_report_filtered_df_combined['CA_ActualFinish'] - ca_report_filtered_df_combined['CA_Start']).dt.days
ca_report_filtered_df_combined['CA_Start_Num'] = (ca_report_filtered_df_combined['CA_Start'] - ca_report_filtered_df_combined['CA_Start'].min()).dt.total_seconds() / (365.25 * 24 * 3600)

# Aggregate milestone data for each CA_ID
aggregated_milestones = milestones_df_combined.groupby('CA_ID').agg({
    'Deviation_From_Plan': 'mean',
    'Deviation_From_BL': 'mean',
    'Reported': 'sum',
    'Visible_In_Gantt': 'sum'
}).reset_index()

# Merge with the main project data
ca_report_filtered_df_combined['Log_Duration'] = np.log1p(ca_report_filtered_df_combined['Duration'])
ca_report_merged_df_combined = pd.merge(ca_report_filtered_df_combined, aggregated_milestones, on='CA_ID', how='left')

# Handle missing values
X = ca_report_merged_df_combined[['CA_Start_Num', 'Deviation_From_Plan', 'Deviation_From_BL', 'Reported', 'Visible_In_Gantt']]
y = ca_report_merged_df_combined['Log_Duration']
X.fillna(0, inplace=True)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the model architecture
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],), kernel_regularizer=l2(0.001)),
    Dropout(0.2),
    Dense(128, activation='relu', kernel_regularizer=l2(0.001)),
    Dropout(0.2),
    Dense(1)  # Output layer for predicting log-transformed duration
])

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='huber', metrics=['mae'])

# Callbacks for early stopping and learning rate reduction
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
lr_scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, min_lr=1e-6)

# Train the model
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, callbacks=[early_stopping, lr_scheduler])

# Evaluate the model on the test data
test_loss, test_mae = model.evaluate(X_test, y_test)
print("Test MAE (on log-transformed data):", test_mae)


# Predicting Tentative Finish Dates
actual_start = pd.to_datetime('2020-01-01')  # Replace with the desired start date
new_data = pd.DataFrame({
    'CA_Start_Num': [(actual_start - ca_report_merged_df_combined['CA_Start'].min()).total_seconds() / (365.25 * 24 * 3600)],
    'Deviation_From_Plan': [0],
    'Deviation_From_BL': [0],
    'Reported': [0],
    'Visible_In_Gantt': [0]
})

# Normalize the new data
new_data = scaler.transform(new_data)

# Make predictions
log_predicted_duration = model.predict(new_data)
predicted_duration_days = np.expm1(log_predicted_duration).flatten()

# Clip to maximum threshold based on training data
max_duration = ca_report_merged_df_combined['Duration'].quantile(0.95)
predicted_duration_days = np.clip(predicted_duration_days, 0, max_duration)

# Calculate tentative finish date
tentative_finish_date = actual_start + pd.to_timedelta(predicted_duration_days, unit='D')
print("Tentative Finish Date:", tentative_finish_date[0])

# Plot training and validation MAE
plt.figure(figsize=(12, 6))
plt.plot(history.history['mae'], label='Training MAE')
plt.plot(history.history['val_mae'], label='Validation MAE')
plt.xlabel('Epochs')
plt.ylabel('MAE')
plt.legend()
plt.show(block = False)