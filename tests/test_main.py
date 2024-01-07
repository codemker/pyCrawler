from lxml.etree import HTML
from requests import get
import pandas as pd
import pytest

def test_data():
    
    numbersbn = []
    ln = []
    url = "https://www.patogupirkti.lt/catalogsearch/result?order=relevance&dir=desc&q='tvarka'"
    resp = get(url)
    tree = HTML(resp.text)
    # Extract the URLs of the books with ElementTree library, lxml extension and xpath() method
    for link in tree.xpath("//div[@class='title']//a/@href"):
        ln.append(link)
        data = get(link)
        treebr = HTML(data.text)
        for book_isbn in treebr.xpath("//ul[@class='details-list mt5']/li[6]//span"):
            numbr = book_isbn.text
            numbersbn.append(numbr)
    print(numbersbn)
    
    assert True

test_data()
    




