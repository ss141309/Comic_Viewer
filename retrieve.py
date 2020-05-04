from bs4 import BeautifulSoup
import re
import cloudscraper

scraper = cloudscraper.create_scraper()

baseURL = 'https://readcomiconline.to'

def retrieve(name):
    url = baseURL + '/Search/Comic/' + name
    search_page = scraper.get(url)

    soup = BeautifulSoup(search_page.content,'html.parser')
    id = soup.find(id='container')
    titles = id.find_all('a',href=re.compile('/Comic/.*'))

    for i in enumerate(titles):
        if 'Issue' not in i[1].text:
            print((i[1].text.strip()))

k = retrieve('star wars')
print(k)
