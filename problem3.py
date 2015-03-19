#! /usr/bin/python

from bs4 import BeautifulSoup
from urllib import urlopen

# given the url, fetch and return the html source using urlopen
def get_page_source(url):
    f = urlopen(url)
    source = f.read()
    f.close()
    return source

# use BeautifulSoup to extract headlines from the raw html 
def extract_news_headlines(html_source):
    headlines = []
    soup = BeautifulSoup(html_source)
    divs = soup.findAll("div", "row db-list")
    for div in divs:
        articles = div.findAll("article", "post")
        for article in articles:
            header = article.find("h2")
            link = header.find("a")
            headlines.append(link.getText())
    return headlines

def main():
    html_source = get_page_source("http://dailybruin.com/category/news/")
    headlines = extract_news_headlines(html_source)
    for headline in headlines:
        print headline

if __name__ == '__main__':
    main()