from bs4 import BeautifulSoup
import re
import cloudscraper
from img_download import dwnld_batch
import retrieve_search

baseURL = 'https://readcomiconline.to/Comic/'

def urlify(s): # credit of https://stackoverflow.com/questions/1007481/how-do-i-replace-whitespaces-with-underscore-and-vice-versa

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)

    return s

class retrieve_info:
    def __init__(self, title):
        self.title = title

    def publisher(self):

        url = baseURL + self.title()

        data = retrieve_search.web_scraper(url)

        publisher = data.find_all('p')

        for pub in publisher:
            print(str(pub.text).split('\n'))

m = urlify('Wolverine Annual 2 Bloodlust')
k = retrieve_info.publisher(m)
print(k)
