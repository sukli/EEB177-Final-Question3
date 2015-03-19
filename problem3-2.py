#! /usr/bin/python

from bs4 import BeautifulSoup
from urllib import urlopen

# given the url, fetch and return the html source using urlopen
def get_page_source(url):
    f = urlopen(url)
    source = f.read()
    f.close()
    return source

# use BeautifulSoup to extract headline urls from the raw html 
def extract_news_headline_urls(html_source):
    headline_urls = []
    soup = BeautifulSoup(html_source)
    # first find the enclosing divs of the headlines
    divs = soup.findAll("div", "row db-list")
    for div in divs:
        # inside each div, drill down the <a> element which contains the headline text
        articles = div.findAll("article", "post")
        for article in articles:
            header = article.find("h2")
            link = header.find("a")
            # add headline text to list
            headline_urls.append(link["href"])
    return headline_urls

if __name__ == '__main__':
    main()