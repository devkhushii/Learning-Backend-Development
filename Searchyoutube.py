from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# URL to be loaded
url = "https://www.youtube.com/"

# Path to the ChromeDriver executable
chrome_driver_path = "C:/Users/ranik/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Creating a Service object for the ChromeDriver
service = Service(chrome_driver_path)

# Initializing the Chrome WebDriver with the specified service
driver = webdriver.Chrome(service=service)

# Loading the specified URL in the browser
driver.get(url)

# Finding the search box element using its XPath
box = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")

# Typing the search query into the search box
search_query= " bollywood songs"
box.send_keys(search_query)

# Waiting for 2 seconds before submitting the search
time.sleep(2)

# Submitting the search query by pressing the Enter key
box.send_keys(Keys.ENTER)
time.sleep(3)

# Find the first video in the search results and click on it
first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
first_video.click()

# Let the song play for a while
time.sleep(100)  # Change this value to let the song play for a longer duration

# Close the browser
driver.quit()