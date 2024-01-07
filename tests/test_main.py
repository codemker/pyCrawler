import pytest
from crawler import main

def test_crawler():
    mytest1 = main.crawler_query("A", "B", "C", "D")
    print(mytest1)
    assert True



