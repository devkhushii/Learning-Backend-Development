from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# URL to be loaded
url = "https://www.ajio.com/c/830307006"

# Path to the ChromeDriver executable
chrome_driver_path = "C:/Users/ranik/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
# Creating a Service object for the ChromeDriver
service = Service(chrome_driver_path)

# Initializing the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Loading the specified URL in the browser
driver.get(url)

# Waiting for 10 seconds to ensure the initial content is fully loaded
time.sleep(10)

# Getting the initial scroll height of the webpage
height = driver.execute_script("return document.body.scrollHeight")
print(f"Initial height: {height}")

# Entering a loop to scroll down the page and load dynamic content
while True:
    # Scroll to the bottom of the webpage
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # Waiting for 2 seconds to allow new content to load
    time.sleep(2)
    
    # Getting the new scroll height after scrolling
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    # If the scroll height hasn't changed, it means no new content is loaded, so break the loop
    if height == new_height:
        break
    
    # Updating the height for the next iteration
    height = new_height

# Printing completion message
print("Scrolling complete.")