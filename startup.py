from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import os

class Checks(QtWidgets.QWidget):
    cursor: sqlite3.Cursor
    def __init__(self):
        super().__init__()
        self.databaseExists()

    def databaseExists(self):
        if os.path.isfile("database/tc.db"):
            pass
        else:
            database = QMessageBox.warning(
                self,'Database Error', 'Database Not Found. '
                'Do you want to create one',QMessageBox.Yes | QMessageBox.No)
            if database == QMessageBox.Yes:
                self.createDatabase()
            else:
                exit(1)

    def createDatabase(self):
        try:
            self.connection = sqlite3.connect('database/tc.db')
            self.cursor = self.connection.cursor()
            self.createTableInDatabase()
        except Exception as e:
            print(e)
            a = QMessageBox.Warning(self,'Database Error', 'Failed to create database.'
                                'Try running application as administrator')

    def createTableInDatabase(self):
        try:
            query = """CREATE TABLE IF NOT EXISTS class_one(studentId INT(5), name VARCHAR(10), dob TEXT)"""
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print(e)

    def __del__(self):
        pass
