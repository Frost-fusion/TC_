# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Code\Python\TC\TC_\design\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(771, 559)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 10, 221, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 100, 181, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 500, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 50, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 500, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.please = QtWidgets.QPushButton(Form)
        self.please.setGeometry(QtCore.QRect(350, 500, 93, 28))
        self.please.setCheckable(False)
        self.please.setAutoDefault(False)
        self.please.setObjectName("please")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 55, 16))
        self.label_3.setObjectName("label_3")
        self.classLineEdit = QtWidgets.QLineEdit(Form)
        self.classLineEdit.setGeometry(QtCore.QRect(80, 140, 113, 22))
        self.classLineEdit.setObjectName("classLineEdit")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(80, 190, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 55, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Zilla Parishd Primary School"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Student No."))
        self.pushButton.setText(_translate("Form", "Search"))
        self.label_2.setText(_translate("Form", "Name:"))
        self.pushButton_2.setText(_translate("Form", "Update"))
        self.pushButton_3.setText(_translate("Form", "Add New"))
        self.pushButton_4.setText(_translate("Form", "Delete"))
        self.please.setText(_translate("Form", "Print "))
        self.label_3.setText(_translate("Form", "Class"))
        self.label_4.setText(_translate("Form", "Dob"))