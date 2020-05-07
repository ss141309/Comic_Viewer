from bs4 import BeautifulSoup
import re
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

    def info(self):
        global publish
        global write
        global art
        global url
        global data

        url = baseURL + self.title()

        data = retrieve_search.web_scraper(url)

        p = data.find_all('p')

        for inf in p:
            if 'Publisher' in str(inf):
                publish = inf.text

            if 'Writer' in str(inf):
                write = inf.text

            if 'Artist' in str(inf):
                art = inf.text

    def publisher(self):
        retrieve_info.info(self)

        publ = publish.split('Publisher:')[1].strip()

        return publ

    def author(self):
        retrieve_info.info(self)

        writ = write.split('Writer:')[1].strip()

        return writ

    def artist(self):
        retrieve_info.info(self)

        arti = art.split('Artist:')[1].strip()

        return arti

    def chap(self):
        global chap_dict

        chapter_no = []
        chapter_link = []
        retrieve_info.info(self)

        a = data.find_all('a', href = re.compile('/Comic/.*'), title = re.compile('.*'))

        for ele in a:
            chapter_no.append(ele.text.strip())
            chapter_link.append('www.readcomiconline.to' + str(ele).split('href=')[1].split(' title')[0].strip('\"'))

        chap_dict = dict(zip(chapter_link, chapter_no))

        return chap_dict

    def chap_img(self):
        chap_img_list = []

        url = 'https://readcomiconline.to/Comic/Ultimate-Comics-X-Men/Issue-33?id=60395'
        data1 = retrieve_search.web_scraper(url)

        script = data1.find_all('a')
        print(script)

m = urlify('Ultimate Comics X men')
k = retrieve_info.chap_img('https://readcomiconline.to/Comic/Ultimate-Comics-X-Men/Issue-33?id=60395')
print(k)
