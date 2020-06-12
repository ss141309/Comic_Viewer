import sqlite3

conn = sqlite3.connect('comic.db')
def downloaded():
    conn = sqlite3.connect('comic.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS DOWNLOADED
                (ID INTEGER      PRIMARY KEY AUTOINCREMENT NOT NULL,
                TITLE            TEXT NOT NULL,
                PUBLISHER        TEXT,
                WRITER           TEXT,
                ARTIST           TEXT,
                PUBLICATION_DATE  INT,
                IMG_URL          TEXT,
                URL              TEXT,
                IMG_PATH         TEXT,
                SUMMARY           BLOB);''')
    conn.commit()
    conn.close()

def download_chapters():
    conn = sqlite3.connect('comic.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS DOWNLOADED_CHAPTERS
                (CHAPTER_URL TEXT ,
                COMIC_NAME   TEXT,
                CHAPTER_NAME TEXT);''')
    conn.commit()
    conn.close()

def search():
    conn = sqlite3.connect('comic.db')
    conn.execute('''CREATE  TABLE IF NOT EXISTS SEARCH
                (ID             INTEGER PRIMARY KEY NOT NULL,
                TITLE           TEXT,
                PUBLISHER        TEXT,
                WRITER           TEXT,
                ARTIST           TEXT,
                PUBLICATION_DATE  INT,
                IMG_URL          TEXT,
                URL              TEXT,
                IMG_PATH         TEXT,
                SUMMARY           TEXT);''')
    conn.commit()
    conn.close()
def search_dupl():
    conn = sqlite3.connect('comic.db')
    conn.execute('PRAGMA foreign_keys = ON')
    conn.execute('''CREATE  TABLE IF NOT EXISTS SEARCH_DUPL
                (ID             INTEGER PRIMARY KEY ,
                TITLE           TEXT,
                PUBLISHER        TEXT,
                WRITER           TEXT,
                ARTIST           TEXT,
                PUBLICATION_DATE  INT,
                IMG_URL          TEXT,
                URL              TEXT,
                IMG_PATH         TEXT,
                SUMMARY           TEXT,
                FOREIGN KEY (ID)
                REFERENCES SEARCH (ID)
                    ON UPDATE  CASCADE
                    ON DELETE  RESTRICT);''')
    conn.commit()
    conn.close()


def chapters():
    conn = sqlite3.connect('comic.db')
    conn.execute('''CREATE  TABLE IF NOT EXISTS CHAPTERS
                (CHAPTER_URL TEXT,
                COMIC_NAME   TEXT,
                CHAPTER_NAME TEXT);''')
    conn.commit()
    conn.close()
