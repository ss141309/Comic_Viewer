import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget,\
                            QTabWidget, QStackedLayout, QHBoxLayout, QVBoxLayout,\
                            QPushButton, QTableWidget, QLineEdit, QHeaderView, QLabel
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *

import qtmodern.styles
import qtmodern.windows


class ComicUI(QMainWindow):
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


    def table(self):
        self.tabs_wid = QTabWidget()
        self.stack_layout1 = QStackedLayout()
        self.stack_layout2 = QStackedLayout()

        table = []
        for i in range(4):
            self.table = QTableWidget()
            self.table.setColumnCount(2)
            self.table.setRowCount(1000)
            self.table.setFrameStyle(0)
            self.table.setHorizontalHeaderLabels(['S. No.', 'Title'])
            self.header = self.table.horizontalHeader()
            self.header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            self.header.setSectionResizeMode(1, QHeaderView.Stretch)
            self.table.verticalHeader().setVisible(False)

            table.append(self.table)

        self.stack_layout1.addWidget(table[0])
        self.stack_layout1.addWidget(table[1])

        self.stack_layout2.addWidget(table[2])
        self.stack_layout2.addWidget(table[3])


        #Since QTabWidget only accepts a widget, a widget is made with the stacked layout
        tab1 = QWidget()
        tab2 = QWidget()

        button = []
        for j in range(2):
            self.forward = QPushButton()
            self.back = QPushButton()

            self.forward.setText('>')
            self.back.setText('<')

            self.forward.setFixedSize(22,22)
            self.back.setFixedSize(22,22)

            button.extend([self.back, self.forward])

        self.horilayout = QHBoxLayout()
        self.horilayout2 = QHBoxLayout()

        self.horilayout.addWidget(button[0])
        self.horilayout.addWidget(button[1])

        self.horilayout2.addWidget(button[2])
        self.horilayout2.addWidget(button[3])

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
        hlayout = QHBoxLayout()

        self.ledit = QLineEdit()
        self.btn = QPushButton()

        self.ledit.setPlaceholderText('Search')
        self.btn.setText('Ok')

        hlayout.addWidget(self.ledit, 1000)
        hlayout.addWidget(self.btn, 2)

        self.generalLayout.addLayout(hlayout,5,0,2,1)

    def info(self):
        self.vlayout = QVBoxLayout()

        hlay = []
        for lay in range(6):
            self.hlayout = QHBoxLayout()
            hlay.append(self.hlayout)

        labels = []

        names = ['Name:',
                 'Publisher:',
                 'Writer:',
                 'Publication Date:',
                 'Summary:',
                 'Status:']

        for label in range(len(names)):
            self.label = QLabel()
            self.label2 = QLabel()

            labels.append([self.label, self.label2])

            self.label.setText(names[label])

        for sett in range(6):
            hlay[sett].addWidget(labels[sett][0], 1) # Second argument sets the stretch ratio with the other widget
            hlay[sett].addWidget(labels[sett][1], 50)

            hlay[sett].setSpacing(5)

            self.vlayout.addLayout(hlay[sett])

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

class ComicCtrl:
    def __init__(self, view):
        self._view = view

        self._connectSignals()

    def _connectSignals(self):
        self._view.btn.clicked.connect(self.basic)
        self._view.ledit.returnPressed.connect(self.basic)

    def basic(self):
        print('Hello')

def main():
    app = QApplication(sys.argv)

    view = ComicUI()
    #view.show()
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(view)
    mw.show()
    ComicCtrl(view=view)
    sys.exit(app.exec_())

main()
