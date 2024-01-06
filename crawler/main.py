from lxml.etree import HTML
from lxml import etree
from requests import get
import pandas as pd
import csv
import os
import re
import crawl_img

os.makedirs('data', exist_ok=True)
titles = []
authors = []
links = []
    
prices = []
l_authors = []
extracted = []


def crawler_query():
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
        page_url = "https://www.patogupirkti.lt/catalogsearch/result?order=relevance&dir=desc&q='komunikacija'"
        # Get the HTML of the search results page.
        response = get(page_url)
        tree = HTML(response.text)
        for page_link in tree.xpath("//div[@class='title']//a/@href"):
            links.append(page_link)

            data = get(page_link)
            treeim = HTML(data.text)

            treeim = HTML(data.text)
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

            for book_price in treeim.xpath("//div[@class='price-wrapper']//span"):
                price = book_price.text
                prices.append(price.strip())

            # print(f" {page_link} | {title} | {print_list} | {price} ")

            extracted.append({
                "link": page_link,
                "book": title,
                "author": print_list,
                "price": price
            })
        # print(extracted)
        df = pd.DataFrame(extracted)
        print(df)

        # with open('report20.csv', 'w+') as file:
        # for link in links:
        # file.write(f"{link}\n")

        # df.to_csv('data/report.csv', encoding='utf-8', index=False)

    except Exception:
        print("Error retrieving url")


if __name__ == "__main__":
    crawler_query()

    images_save = crawl_img.gets_img()

    def getting_img():
        return images_save

    getting_img()
