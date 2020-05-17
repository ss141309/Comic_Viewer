from bs4 import BeautifulSoup
import re
from retrieve_search import *
import cloudscraper


scraper = cloudscraper.create_scraper()


baseURL = 'https://readeleonline.to'


class retrieve_info:
    def __init__(self, title):
        self.title = title

    def info(self):
        global data
        global url
        global info_list

        info_dict = {}
        info = []
        url = self.title()


        data = web_scraper(url)

        p = data.find_all('p')

        for inf in p:
            if 'Publisher' in str(inf) or 'Writer' in str(inf) or 'Artist' in str(inf) or 'Summary' in str(inf) or 'Publication' in str(inf):
                info.append(inf.text.strip())

        info_list = list(set(info)) # set() removes duplicate element from a list but the order is lost

        return info_list


    def chap(self):

        chapter_no = []
        chapter_link = []

        retrieve_info.info(self)
        div_class = data.find_all('div',class_ = 'barContent')
        div_class = div_class[1]

        a = div_class.find_all('a')

        for ele in a:
            if '/RSS/' not in str(ele): # to remove the RSS link
                chapter_link.append(baseURL + ele['href'].strip())
                chapter_no.append(ele.text.strip())

        chap_dict = dict(zip(chapter_link, chapter_no))

        return chap_dict

    def chap_img(self):

        chap_img_list = []

        url = self.title()
        search_page = scraper.get(url)  # sends a GET request to the page

        soup = BeautifulSoup(search_page.content,'html.parser')

        scripts = soup.find_all('script')

        for script in scripts:
            if 'lstImages.push' in str(script):
                k = (str(script).split('\n'))
                for img_url in k:
                    if 'lstImages.push' in img_url:
                        chap_img_list.append('http'+img_url.lstrip('        lstImages.push("').rstrip('");\r'))

        return chap_img_list
k = retrieve_info.info('https://readcomiconline.to/Comic/Popular-Skullture-The-Skull-Motif-in-Pulps-Paperbacks-and-Comics')
print(k)
