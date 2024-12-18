import torch
import transformers

# Model ID for the specific LLaMA model you want to use
model_id = "meta-llama/Llama-3.2-3B"

# Load the model using the Transformers pipeline
pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},  # Set torch_dtype for efficient GPU usage
    device="cuda" if torch.cuda.is_available() else "cpu",  # Automatically choose GPU if available
)

# Test the model with a sample input
input_text = " current version of llama"
result = pipeline(input_text, max_length=150)

# Print the generated text
print(result[0]['generated_text'])
