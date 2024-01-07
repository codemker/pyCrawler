from lxml.etree import HTML
from requests import get
import pandas as pd
import csv
import os
from crawlerext import crawl_img
#import sys
#sys.path.append("/crawlerext")

os.makedirs('data', exist_ok=True)
titles = []
authors = []
links = []   
prices = []
l_authors = []
extracted = []

def crawler_query(l: str, t: str, a: str, p: str)  -> list :
    """
    This function crawls the website search results for books and retrieves the URLs, titles, authors, and prices of the top 10 results.

    Returns:
        A list of dictionaries, where each dictionary has the following keys:
            - url: The URL of the book
            - title: The title of the book
            - author: The author of the book
            - price: The price of the book
    """
    try:
        # Get the HTML of the search results page.
        page_url = "https://www.patogupirkti.lt/catalogsearch/result?order=relevance&dir=desc&q='komunikacija'"
        response = get(page_url)
        tree = HTML(response.text)
        # Extract the URLs of the books with ElementTree library, lxml extension and xpath() method
        for page_link in tree.xpath("//div[@class='title']//a/@href"):
            links.append(page_link)
            data = get(page_link)
            treeim = HTML(data.text)
            # Extract the titles of the books with ElementTree library, lxml extension and xpath() method
            for book_title in treeim.xpath("//h1"):
                title = book_title.text
                titles.append(title.strip())
            for book_author in treeim.xpath("//div[@class='author']//span"):
                author = book_author.text
                authors.append(author)
            authors.append("!")
            next_list = []
            lst_authors = []
            spr = "!"
            # Extract the authors of the books with ElementTree library, lxml extension and xpath() method
            for lst_author in authors:
                if lst_author == spr:
                    next_list.append(lst_author)
                    next_list.remove(spr)
                    lst_authors.append(next_list)
                    n_list = next_list
                    sprt = " - "
                    print_list = sprt.join(n_list)
                    next_list = []
                else:
                    next_list.append(lst_author.strip())
            lst_authors.append(next_list)
            l_authors.append(print_list)
            # Extract the prices of the books with ElementTree library, lxml extension and xpath() method
            for book_price in treeim.xpath("//div[@class='price-wrapper']//span"):
                price = book_price.text
                prices.append(price.strip())

            # print(f" {page_link} | {title} | {print_list} | {price} ")
            extracted.append({
                l : page_link,
                t : title,
                a : print_list,
                p : price
            })
        
        return extracted    

    except Exception:
        print("Error retrieving url")

if __name__ == "__main__":
    web_data = crawler_query("Link", "Title", "Author", "Price")
    df = pd.DataFrame(web_data)
    # Ask the user if they would like to save the data to a CSV file. If the "Y" entered, code will save the data to a CSV file and then exit the loop.
    while True:
        saveCsv = input("Would yuo like to save data to cvs file Y/N ? ")   
        if  saveCsv == "Y":
            df.to_csv('data/report.csv', encoding='utf-8', index=False)
            print("Books cvs file is saved")
            print(df)
            break
        elif saveCsv  == "N":
            print("Books cvs file is not saved")
            print(df)
            break
        else:
            print("Type 'Y' for Yes and 'N' for No")
    """
    images_save = getimg.get_img(4)
    def getting_img():
        return images_save
    """   
    # Ask the user if they would like to save images. If the "Y" entered, code will save the images to the PC and then exit the loop.
    while True:
        saveCsv = input("Would yuo like to save books images Y/N ? ")
        if saveCsv == "Y":
            crawl_img.gets_img(3)
            print("Books images are saved")
            break
        elif saveCsv == "N":
            print("Books images are not saved")
            break
        else:
            print("You typed Y/N ?")
