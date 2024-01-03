from lxml.etree import HTML
from lxml import etree
from requests import get
import pandas as pd
import csv
import crawl_img 

titles = []#
authors = []
links = []
prices = []
l_authors = []
def crawler_query():
    try:
        page_url = "https://www.patogupirkti.lt/catalogsearch/result?order=relevance&dir=desc&q='komunikacija'"
                    
        response = get(page_url)
        tree = HTML(response.text)
    
        
        for page_link in tree.xpath("//div[@class='title']//a/@href"):
            #print(page_link)
            links.append(page_link)
            
            data = get(page_link)
            treeim = HTML(data.text)
        
            treeim = HTML(data.text)
            for book_title in treeim.xpath("//h1"):
                title = book_title.text
                #print(f" {title} {page_link}")
                titles.append(title.strip()) 
            for book_author in treeim.xpath("//div[@class='author']//span"):
                author = book_author.text #
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
                    sprt = " "
                    print_list = sprt.join(n_list)
                    next_list = []
                else:
                    next_list.append(lst_author.strip())
            lst_authors.append(next_list)
            l_authors.append(print_list)
              
            for book_price in treeim.xpath("//div[@class='price-wrapper']//span"):
                price = book_price.text
                prices.append(price.strip())
                
            print(f" {page_link} | {title} | {print_list} | {price} ")       
       
        
        with open('report20.csv', 'w+') as file:
            for link in links:
                file.write(f"{link}\n")
    except Exception:
        print("Error retrieving url")
        

if __name__ == "__main__":
    crawler_query()

    images_save = crawl_img.gets_img()

    def geting_img():
        return images_save

    geting_img()
