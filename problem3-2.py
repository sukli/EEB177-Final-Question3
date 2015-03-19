#! /usr/bin/python

from bs4 import BeautifulSoup
from urllib import urlopen

# given the url, fetch and return the html source using urlopen
def get_page_source(url):
    f = urlopen(url)
    source = f.read()
    f.close()
    return source

# use BeautifulSoup to extract headline text and url from the raw html 
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
            headline_urls.append((link.getText(), link["href"]))
    return headline_urls

# count the paragraphs of the news story
def count_paragraphs(html_source):
    soup = BeautifulSoup(html_source)
    # the paragraph elements of interest are located under the div.db-post-content element
    story_div = soup.find("div", "db-post-content")
    return len(story_div.findAll("p"))

def main():
    base_url = "http://dailybruin.com"
    # retrieve the source and pass it through to the extraction function
    html_source = get_page_source("http://dailybruin.com/category/news/")
    headlines = extract_news_headline_urls(html_source)
    for (headline_text, headline_url) in headlines:
        story_html_source = get_page_source(base_url + headline_url)
        paragraph_count = count_paragraphs(story_html_source)
        print "%s: %d" % (headline_text, paragraph_count)

if __name__ == '__main__':
    main()