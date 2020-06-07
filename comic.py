import sys
import os
import sqlite3
import re

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qtmodern.styles
import qtmodern.windows

from retrieve_search import info
from retrieve_chap import retrieve_info
from main import tables
import img_download
import makedir

class comic_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Comic Viewer')
        self.setGeometry(300, 50, 1600, 950)

        self.generalLayout = QGridLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self.table()
        self.search()
        self.info()
        self.conn()

    def table(self):
        self.tabs_wid = QTabWidget()
        self.stack_layout1 = QStackedLayout()
        self.stack_layout2 = QStackedLayout()

        #Table 1
        self.table1 = QTableWidget()
        self.table1.setColumnCount(2)
        self.table1.setRowCount(1000)
        self.table1.setFrameStyle(0)
        self.table1.setHorizontalHeaderLabels(['S. No.', 'Title'])
        self.header = self.table1.horizontalHeader()
        self.header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.table1.verticalHeader().setVisible(False)

        #Table 2
        self.table2 = QTableWidget()
        self.table2.setColumnCount(2)
        self.table2.setRowCount(1000)
        self.table2.setFrameStyle(0)
        self.table2.setHorizontalHeaderLabels(['S. No.', 'Chapter'])
        self.header = self.table2.horizontalHeader()
        self.header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.table2.verticalHeader().setVisible(False)

        #Table 3
        self.table3 = QTableWidget()
        self.table3.setColumnCount(2)
        self.table3.setRowCount(1000)
        self.table3.setFrameStyle(0)
        self.table3.setHorizontalHeaderLabels(['S. No.', 'Title'])
        self.header = self.table3.horizontalHeader()
        self.header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.table3.verticalHeader().setVisible(False)

        #Table 4
        self.table4 = QTableWidget()
        self.table4.setColumnCount(2)
        self.table4.setRowCount(1000)
        self.table4.setFrameStyle(0)
        self.table4.setHorizontalHeaderLabels(['S. No.', 'Chapter'])
        self.header = self.table4.horizontalHeader()
        self.header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.table4.verticalHeader().setVisible(False)

        self.stack_layout1.addWidget(self.table1)
        self.stack_layout1.addWidget(self.table2)

        self.stack_layout2.addWidget(self.table3)
        self.stack_layout2.addWidget(self.table4)


        #Since QTabWidget only accepts a widget, a widget is made with the stacked layout
        tab1 = QWidget()
        tab2 = QWidget()

        self.forward = QPushButton()
        self.back = QPushButton()
        self.forward2 = QPushButton()
        self.back2 = QPushButton()

        self.forward.setText('>')
        self.back.setText('<')
        self.forward.setFixedSize(22,22)
        self.back.setFixedSize(22,22)

        self.forward2.setText('>')
        self.back2.setText('<')
        self.forward2.setFixedSize(22,22)
        self.back2.setFixedSize(22,22)

        self.horilayout = QHBoxLayout()
        self.horilayout2 = QHBoxLayout()

        self.horilayout.addWidget(self.back)
        self.horilayout.addWidget(self.forward)

        self.horilayout2.addWidget(self.back2)
        self.horilayout2.addWidget(self.forward2)

        self.vertlayout = QGridLayout()
        self.vertlayout.addLayout(self.horilayout,0,5)
        self.vertlayout.addLayout(self.stack_layout1,1,0,1,6)

        self.vertlayout2 = QGridLayout()
        self.vertlayout2.addLayout(self.horilayout2,0,5)
        self.vertlayout2.addLayout(self.stack_layout2,1,0,1,6)

        tab1.setLayout(self.vertlayout)
        tab2.setLayout(self.vertlayout2)


        self.tabs_wid.addTab(tab1,'Download')
        self.tabs_wid.addTab(tab2,'Downloaded')

        self.generalLayout.addWidget(self.tabs_wid,0,0,1,6)

    def search(self):
        self.hlayout = QHBoxLayout()

        self.ledit = QLineEdit()
        self.btn = QPushButton()

        self.ledit.setPlaceholderText('Search')
        self.btn.setText('Ok')

        self.hlayout.addWidget(self.ledit, 1000)
        self.hlayout.addWidget(self.btn, 2)

        self.generalLayout.addLayout(self.hlayout,5,0,2,1)

    def info(self):
        self.vlayout = QVBoxLayout()
        self.hlayout1 = QHBoxLayout()
        self.hlayout2 = QHBoxLayout()
        self.hlayout3 = QHBoxLayout()
        self.hlayout4 = QHBoxLayout()
        self.hlayout5 = QHBoxLayout()
        self.hlayout6 = QHBoxLayout()

        self.label1 = QLabel()
        self.label1_1 = QLabel()
        self.label2 = QLabel()
        self.label2_1 = QLabel()
        self.label3 = QLabel()
        self.label3_1 = QLabel()
        self.label4 = QLabel()
        self.label4_1 = QLabel()
        self.label5 = QLabel()
        self.label5_1 = QLabel()
        self.label6 = QLabel()
        self.label6_1 = QLabel()

        self.label1_1.setAlignment(Qt.AlignLeft)

        self.label1.setText('Name:')
        self.label2.setText('Publisher:')
        self.label3.setText('Writer:')
        self.label4.setText('Artist:')
        self.label5.setText('Publication Date:')
        self.label6.setText('Summary:')


        self.hlayout1.addWidget(self.label1, 1) # Second argument sets the stretch ratio with the other widget
        self.hlayout1.addWidget(self.label1_1, 50)
        self.hlayout2.addWidget(self.label2, 1)
        self.hlayout2.addWidget(self.label2_1, 50)
        self.hlayout3.addWidget(self.label3, 1)
        self.hlayout3.addWidget(self.label3_1, 50)
        self.hlayout4.addWidget(self.label4, 1)
        self.hlayout4.addWidget(self.label4_1, 50)
        self.hlayout5.addWidget(self.label5, 1)
        self.hlayout5.addWidget(self.label5_1, 50)
        self.hlayout6.addWidget(self.label6, 1)
        self.hlayout6.addWidget(self.label6_1, 50)

        self.hlayout1.setSpacing(5)
        self.hlayout2.setSpacing(5)
        self.hlayout3.setSpacing(5)
        self.hlayout4.setSpacing(5)
        self.hlayout5.setSpacing(5)
        self.hlayout6.setSpacing(5)

        self.vlayout.addLayout(self.hlayout1)
        self.vlayout.addLayout(self.hlayout2)
        self.vlayout.addLayout(self.hlayout3)
        self.vlayout.addLayout(self.hlayout4)
        self.vlayout.addLayout(self.hlayout5)
        self.vlayout.addLayout(self.hlayout6)
        self.vlayout.setSpacing(25)


        self.generalLayout.addLayout(self.vlayout,7,0)

    def img(self, img_path):
        frame = QWidget()
        label_Image = QLabel(frame)
        image_path = img_path #path to your image file
        image_profile = QImage(image_path) #QImage object
        image_profile = image_profile.scaled(250,250, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration
        label_Image.setPixmap(QPixmap.fromImage(image_profile))

        self.generalLayout.addWidget(label_Image, 6, 1,4,5)

    def conn(self):
        self.btn.clicked.connect(self.tab1_info)
        self.ledit.returnPressed.connect(self.tab1_info)

        self.table1.cellDoubleClicked.connect(self.cell_was_clicked)
        self.table2.cellDoubleClicked.connect(self.cell2_was_clicked)

        self.forward.clicked.connect(lambda : self.btn_was_clicked(1, self.stack_layout1))
        self.back.clicked.connect(lambda : self.btn_was_clicked(0, self.stack_layout1))

        self.forward2.clicked.connect(lambda : self.btn_was_clicked(1, self.stack_layout2))
        self.back2.clicked.connect(lambda : self.btn_was_clicked(0, self.stack_layout2))


    def btn_was_clicked(self, index, lay_out):
        lay_out.setCurrentIndex(index)
        self.conn = sqlite3.connect('comic.db')
        self.conn.execute('DELETE FROM CHAPTERS')
        self.conn.commit()
        self.conn.close()

    def tab1_info(self):
        search_term = self.ledit.text()
        self.ledit.setText('')
        a=tables()
        a.download(search_term)
        self.conn = sqlite3.connect('comic.db')
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT ID, TITLE FROM SEARCH_DUPL')
        self.records = self.cur.fetchall()
        self.cur.execute('DELETE FROM SEARCH')
        self.conn.commit()
        self.conn.close()
        for i in enumerate(self.records):
            d = 0
            self.table1.setItem(i[0], d, QTableWidgetItem(str(i[1][0])))
            item = QTableWidgetItem(i[1][1])
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled) # set items not editable
            self.table1.setItem(i[0], d+1, item)
            d += i[0]

    def cell_was_clicked(self):
        self.row = self.table1.currentRow()
        self.conn = sqlite3.connect('comic.db')
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT URL FROM SEARCH_DUPL WHERE ID = ?', (str(self.row+1),))
        self.url = self.cur.fetchall()
        item = tables()
        item.add_info(self.url[0][0])
        self.cur.execute('SELECT TITLE, PUBLISHER, WRITER, ARTIST, PUBLICATION_DATE, SUMMARY, IMG_URL FROM SEARCH_DUPL WHERE ID = ?', (str(self.row+1),))
        self.addit = self.cur.fetchall()

        self.label1_1.setText(self.addit[0][0])
        self.label2_1.setText(self.addit[0][1])
        self.label3_1.setText(self.addit[0][2])
        self.label4_1.setText(self.addit[0][3])
        self.label5_1.setText(self.addit[0][4])
        self.label6_1.setText(self.addit[0][5])

        try: #imgs once downloaded need not be downloaded twice
            image_url = self.addit[0][6]
            dirnme = os.path.abspath('img'+'/'+'thumbnails')
            title = re.sub('[^a-zA-Z0-9 \n\.]', '', self.addit[0][0])
            makedir.mkdirs(dirnme)
            img_download.img_dwnld(image_url, dirnme, title)

            self.cur.execute('UPDATE SEARCH_DUPL SET IMG_PATH = ? WHERE ID = ?', (os.path.join(dirnme, title+'.jpg'), str(self.row+1)))
            self.conn.commit()

            self.cur.execute('SELECT IMG_PATH FROM SEARCH_DUPL WHERE ID = ?', (str(self.row+1),))
            img_path = self.cur.fetchall()
            self.img(os.path.join(img_path[0][0]))
        except:
            self.cur.execute('SELECT IMG_PATH FROM SEARCH_DUPL WHERE ID = ?', (str(self.row+1),))
            img_path = self.cur.fetchall()
            print(img_path[0][0])
            self.img(os.path.join(img_path[0][0]))

        self.stack_layout1.setCurrentIndex(1)
        self.chapters = tables()
        self.chapters.chaps(self.url[0][0], self.addit[0][0])

        self.cur.execute('SELECT CHAPTER_NAME FROM CHAPTERS')
        chptrs = self.cur.fetchall()

        for chptr in enumerate(chptrs):
            d = 0
            self.table2.setItem(chptr[0], d, QTableWidgetItem(str(chptr[0]+1)))
            item = QTableWidgetItem(chptr[1][0])
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled) # set items not editable
            self.table2.setItem(chptr[0], d+1, item)
            d += chptr[0]

        self.conn.close()

    def cell2_was_clicked(self):
        imgs = tables()
        self.row = self.table2.currentRow()
        conn = sqlite3.connect('comic.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM CHAPTERS WHERE rowid = ?', (self.row+1,))
        chptr_url = cur.fetchall()
        cur.execute('INSERT INTO DOWNLOADED_CHAPTERS SELECT * FROM CHAPTERS WHERE CHAPTER_URL = ?', (chptr_url[0][0],))
        cur.execute('INSERT INTO DOWNLOADED SELECT TITLE, PUBLISHER, WRITER, ARTIST, PUBLICATION_DATE, IMG_URL, URL, IMG_PATH, SUMMARY FROM SEARCH_DUPL WHERE TITLE = ?', (chptr_url[0][1],))
        conn.commit()
        conn.close()
        imgs.download_chap(chptr_url[0][0], chptr_url[0][1], chptr_url[0][2])




def main():
    app = QApplication(sys.argv)

    view = comic_ui()
    view.show()
    #qtmodern.styles.dark(app)
    #mw = qtmodern.windows.ModernWindow(view)
    #mw.show()

    sys.exit(app.exec_())

main()
