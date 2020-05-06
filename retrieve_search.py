from bs4 import BeautifulSoup
import re
import cloudscraper
from img_download import dwnld_batch

scraper = cloudscraper.create_scraper() # returns a CloudScraper instance

baseURL = 'https://readcomiconline.to'

def web_scraper(url):
    search_page = scraper.get(url)  # sends a GET request to the page

    soup = BeautifulSoup(search_page.content,'html.parser')

    div_id = soup.find(id='container') # finds the id:container
    return div_id

class retrieve:
    def __init__(self, title):
        self.title = title

    def title(self):
        name_list = []

        url = baseURL + '/Search/Comic/' + self.title()

        data = web_scraper(url)

        titles = data.find_all('a',href = re.compile('/Comic/.*')) # finds all the <a> tag where the href starts with /Comic/

        for name in enumerate(titles):
            if 'Issue' not in name[1].text: # Issue nos. were appearing as comic titles
                name_list.append(name[1].text.strip())
        return name_list

    def thumbnail(self):
        thumb_list=[]

        url = baseURL + '/Search/Comic/' + self.title()

        data = web_scraper(url)
        tags = data.find_all('td') # img tag is contained in an atr of <td>

        for src in tags:
            if 'img' in str(src):
                thumb_list.append(str(src).split('style')[0].split('src="')[1].rstrip('" ')) # extracting the url from the mess
        for thumb_url in enumerate(thumb_list):
            thumb_list[thumb_url[0]] = baseURL + thumb_list[thumb_url[0]]

        return thumb_list

    def desc(self):
        desc_list = []

        url = baseURL + '/Search/Comic/' + self.title()

        data = web_scraper(url)
        tags = data.find_all('td')

        for p in tags:
            if 'img' in str(p):
                desc_list.append(str(p).split('&lt;p&gt;')[1].split('&lt;/p&gt;')[0].strip())

        return desc_list
k = retrieve.thumbnail('joker')
dwnld_batch(k, r'C:\Users\Sameer\Desktop\Comic_Viewer\img\thumbnail')
