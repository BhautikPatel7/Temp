from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to Edge WebDriver
webdriver_path = r"C:\Users\bhautik.thummar\Downloads\edgedriver_win64 (2)\msedgedriver.exe"
service = Service(executable_path=webdriver_path)

# Path to your Edge user data directory
user_data_dir = r"C:\Users\bhautik.thummar\AppData\Local\Microsoft\Edge\User Data"

# Set up options
options = Options()
options.add_argument(f"--user-data-dir={user_data_dir}")  # Use your Edge profile
options.add_argument("--start-maximized")  # Optional: Start maximized
options.add_argument("--remote-debugging-port=9222")  # Optional for debugging
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
# Initialize WebDriver
driver = webdriver.Edge(service=service, options=options)

# Open Bing
driver.get("https://www.bing.com")

# List of 90 words to search
words_to_search = [
    "apple", "banana", "cherry", "dog", "elephant", "flower", "grape", "hat", "ice cream", "jellyfish",
    "kiwi", "lemon", "mango", "notebook", "orange", "parrot", "quilt", "rose", "sunflower", "tree",
    "umbrella", "violet", "watermelon", "xylophone", "yellow", "zebra", "airplane", "beach", "carrot",
    "dinosaur", "earth", "fish", "guitar", "horizon", "insect", "jump", "kite", "lion", "moon",
    "night", "octopus", "peach", "question", "rocket", "sky", "tiger", "universe", "volcano", "wind",
    "xenon", "yacht", "zoom", "abacus", "boat", "cactus", "diamond", "elephant", "fence", "grapes",
    "honey", "ice", "jungle", "kangaroo", "leaves", "mirror", "nest", "orange", "pumpkin", "quicksand",
    "rose", "snow", "telescope", "underwater", "vulture", "water", "x-ray", "yellowstone", "zookeeper",
    "albatross", "balloon", "cloud", "doghouse", "engine", "flame", "giraffe", "halo", "illusion", "jackal",
    "kite", "leopard", "mountain", "nightmare", "octagon", "pyramid", "quill", "raccoon", "snowman",
    "teapot", "unicorn", "vulture", "wool", "xmas", "yawn", "zeppelin", "air", "blueberry", "cactus"
]

# Perform searches
for index, word in enumerate(words_to_search, start=1):
    try:
        # Find the search box and enter the word
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()  # Clear any previous text
        search_box.send_keys(word)  # Enter the word
        search_box.send_keys(Keys.RETURN)  # Press 'Enter'
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait for 2 seconds before the next search
        time.sleep(10)

        print(f"Search {index}: {word} completed.")
    except Exception as e:
        print(f"Error during search {index}: {word}. Exception: {e}")
        continue  # Continue with the next word

# Close the browser after all searches
driver.quit()
