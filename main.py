from retrieve_search import info
from retrieve_chap import retrieve_info
from makedir import *
from img_download import dwnld_batch
import table
import sqlite3

import re
import os

class tables:
    def download(self, name):
        self.conn = sqlite3.connect('comic.db')
        table.search()
        table.search_dupl()
        self.name = name
        find = info(self.name)
        id_no=1
        self.conn.execute('DELETE FROM SEARCH_DUPL')
        for i in find:
            self.conn.execute('INSERT INTO SEARCH (ID, TITLE, IMG_URL, URL, SUMMARY) VALUES (?, ?, ?, ?, ?)',(id_no, i[-1], i[0], i[-2], i[1]))
            self.conn.execute('INSERT INTO SEARCH_DUPL (ID, TITLE, IMG_URL, URL, SUMMARY) VALUES (?, ?, ?, ?, ?)',(id_no, i[-1], i[0], i[-2], i[1]))
            id_no+=1
        self.conn.commit()
        self.conn.close()


    def add_info(self, url):
        self.conn = sqlite3.connect('comic.db')
        table.chapters()
        self.url = url
        k = retrieve_info.info(self.url)

        publisher = k[0].split('Publisher:')[1]
        writer = k[1].split('Writer:')[1]
        artist = k[2].split('Artist:')[1]
        pub_date = k[3].split('Publication date:')[1]

        self.conn.execute('''UPDATE SEARCH SET PUBLISHER = ?, WRITER = ?, ARTIST = ?, PUBLICATION_DATE = ?
                        WHERE URL = ?''',
                        (publisher, writer, artist, pub_date, self.url))
        self.conn.execute('''UPDATE SEARCH_DUPL SET PUBLISHER = ?, WRITER = ?, ARTIST = ?, PUBLICATION_DATE = ?
                        WHERE URL = ?''',
                        (publisher, writer, artist, pub_date, self.url))
        self.conn.commit()

    def chaps(self, url, title):
        self.conn = sqlite3.connect('comic.db')
        self.url = url
        self.title = title
        chapters = retrieve_info.chap(self.url)

        chapters_val = list(chapters.keys())
        chapters_val2 = list(chapters.values())
        chapters_val = chapters_val[::-1]
        chapters_val2 = chapters_val2[::-1]
        for j in range(len(chapters_val)):
            self.conn.execute('INSERT INTO CHAPTERS VALUES (?, ?, ?)', (chapters_val[j], self.title, chapters_val2[j]))
        self.conn.commit()
        self.conn.close()
    def download_chap(self, url, comic_name, chptr_name):
        table.downloaded()
        table.download_chapters()

        self.url = url
        self.comic_name = comic_name
        self.chptr_name = chptr_name

        dw = retrieve_info.chap_img(self.url)

        dic = re.sub('[^a-zA-Z0-9 \n\.]', '', self.comic_name)
        dic2 = re.sub('[^a-zA-Z0-9 \n\.]', '', self.chptr_name)

        d = os.path.abspath('img'+'/'+dic+'/'+dic2)
        mkdirs(d)
        dwnld_batch(dw, d)
