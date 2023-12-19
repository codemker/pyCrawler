from lxml.etree import HTML
from requests import get

links = []
def crawler_query():
    try:
        page_url = "https://www.patogupirkti.lt/catalogsearch/result?order=relevance&dir=desc&q='komunikacija'"
        response = get(page_url)
        tree = HTML(response.text)
        for page_link in tree.xpath("//div[@class='title']//a/@href"):
            full_page_url = "www.patogupirkti.lt" + page_link
            print(full_page_url)
            links.append(full_page_url)
        with open('report.csv', 'w') as file:
            for link in links:
                file.write(f"{link}\n")
    except Exception:
        print("Error retrieving url")


if __name__ == "__main__":
  crawler_query()