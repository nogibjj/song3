from PySide6 import QtCore, QtGui, QtWidgets
import sqlite3
import random

class Alarm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Alarm, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle("Alarm")
        self.resize(420, 290)
        self.old_pos = 0

        self.list = QtWidgets.QListWidget(self)
        self.list.setGeometry(15, 15, 390, 200)

        self.datetimeedit = QtWidgets.QDateTimeEdit(self)
        self.datetimeedit.setGeometry(15, 235, 190, 35)
        self.currentDateTime = QtCore.QDateTime.currentDateTime()
        print(self.currentDateTime)
        
        self.datetimeedit.setDateTime(self.currentDateTime)
        self.datetimeedit.setDisplayFormat("yyyy-MM-dd hh:mm")

        btn_add = QtWidgets.QPushButton("Add Alarm", self)
        btn_add.setGeometry(240, 237, 80, 30)
        btn_add.clicked.connect(self.add)

        btn_del = QtWidgets.QPushButton("Delete Selection", self)
        btn_del.setGeometry(325, 237, 80, 30)
        btn_del.clicked.connect(self.delete)
    
    def add(self):
        pass

    def delete(self):
        pass