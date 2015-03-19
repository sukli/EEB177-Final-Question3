#! /usr/bin/python

from bs4 import BeautifulSoup
from urllib import urlopen

# given the url, fetch and return the html source using urlopen
def get_page_source(url):
    f = urlopen(url)
    source = f.read()
    f.close()
    return source

if __name__ == '__main__':
    main()