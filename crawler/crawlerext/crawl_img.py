import io
from pathlib import Path
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver
import random
import time

# Initialize the Chrome webdriver
driver = webdriver.Chrome()
# Open the webpage
driver.get(
    "https://www.patogupirkti.lt/catalogsearch/result?order=relevance&dir=desc&q='komunikacija'")
time.sleep(1)

# Collect all loaded data
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # scrolling once code
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # wait for content to load
    time.sleep(1)

    # checking new height of webpage
    new_height = driver.execute_script("return document.body.scrollHeight")

    # defining the break condition to stop the execution at the end of the webpage
    if new_height == last_height:
        break
    last_height = new_height

# driver.implicitly_wait(10)
results = []
# Get the HTML content
content = driver.page_source
# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

time.sleep(3)
def gets_img(nbr):
    # find all elements with the specified class attribute.
    for clss in soup.findAll(attrs={"class": "photo"}):
        # Get the image element
        imgg = clss.find("img")
        # Get the image URL
        image = imgg.get("src")
        results.append(image)
    for i in results[0:nbr]:
        # Download the image from the URL
        image_get = requests.get(i).content
        # Create a BytesIO object from the image data
        image_bytes = io.BytesIO(image_get)
        # Open the image from the BytesIO object
        image = Image.open(image_bytes)
        # Create a random file path
        file_path = Path(
            './images', str(random.randrange(1000, 1200)) + ".jpg")
        # Save the image to the file path
        image.save(file_path)

driver.quit()

