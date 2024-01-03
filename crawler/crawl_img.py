import hashlib
import io
from pathlib import Path
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver
from lxml.etree import HTML
import random

driver = webdriver.Chrome()
driver.get("https://www.patogupirkti.lt/catalogsearch/result?order=relevance&dir=desc&q='komunikacija'")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

def gets_img():
    results = []
    for clss in soup.findAll(attrs={"class": "photo"}):
        imgg = clss.find("img")
        images = imgg.get("src")
        image_get = requests.get(images).content
        image_bytes = io.BytesIO(image_get)
        image = Image.open(image_bytes)
        file_path = Path('./images', str(random.randrange(200, 1000)) + ".jpg")
        image.save(file_path)
               
driver.quit()

gets_img()
    
   
      
        