from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator
import sys
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(20, 60, 47, 13)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(20, 90, 47, 13)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(20, 120, 71, 16)
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(20, 150, 47, 13)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(100, 60, 113, 20)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(QRegExpValidator(QRegExp("[a-zA-ZçÇğĞıİöÖşŞüÜ]+")))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(100, 90, 113, 20)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setValidator(QRegExpValidator(QRegExp("[a-zA-ZçÇğĞıİöÖşŞüÜ]+")))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(100, 120, 113, 20)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setValidator(QIntValidator())
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setGeometry(100, 150, 113, 20)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["1. sınıf", "2. sınıf", "3. sınıf", "4. sınıf"])
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(230, 60, 551, 281)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(['Ad', 'Soyad', 'Okul Numarası', 'Sınıf'])
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(110, 190, 75, 23)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: green")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(230, 350, 75, 23)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: red")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(670, 0, 75, 23)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(500, 350, 181, 20)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(700, 350, 75, 23)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(670, 30, 75, 23)
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(480, 0, 181, 22)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["Tümü", "1. sınıf", "2. sınıf", "3. sınıf", "4. sınıf"])
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Öğrenci Bilgi Paneli"))
        self.label.setText(_translate("MainWindow", "Ad"))
        self.label_2.setText(_translate("MainWindow", "Soyad"))
        self.label_3.setText(_translate("MainWindow", "Okul Numarası"))
        self.label_4.setText(_translate("MainWindow", "Sınıf"))
        self.pushButton.setText(_translate("MainWindow", "Kayıt Ekle"))
        self.pushButton_2.setText(_translate("MainWindow", "Kayıt Sil"))
        self.pushButton_3.setText(_translate("MainWindow", "Filtrele"))
        self.pushButton_4.setText(_translate("MainWindow", "Kayıt Ara"))
        self.pushButton_5.setText(_translate("MainWindow", "Temizle"))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.baglanti_olustur()
        self.verileri_getir()

        self.pushButton.clicked.connect(self.kayit_ekle)
        self.pushButton_2.clicked.connect(self.kayit_sil)
        self.pushButton_3.clicked.connect(self.filtrele)
        self.pushButton_4.clicked.connect(self.kayit_ara)
        self.pushButton_5.clicked.connect(self.temizle)

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("veritabani.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kullanici (ad TEXT, soyad TEXT, okul_numarasi TEXT, sinif TEXT)")
        self.baglanti.commit()

    def kayit_ekle(self):
        ad = self.lineEdit.text()
        soyad = self.lineEdit_2.text()
        okul_numarasi = self.lineEdit_3.text()
        
        if ad.strip() == '' or soyad.strip() == '' or okul_numarasi.strip() == '':
            QtWidgets.QMessageBox.warning(self, 'Uyarı', 'Lütfen tüm bilgileri eksiksiz girin!')
            return

        sinif = self.comboBox.currentText()

        self.cursor.execute("INSERT INTO kullanici VALUES (?, ?, ?, ?)", (ad, soyad, okul_numarasi, sinif))
        self.baglanti.commit()
        self.verileri_getir()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

    def kayit_sil(self):
        satir = self.tableWidget.currentRow()
        if satir >= 0:
            okul_numarasi_item = self.tableWidget.item(satir, 2)
            if okul_numarasi_item is not None:
                okul_numarasi = okul_numarasi_item.text()
                self.tableWidget.removeRow(satir)
                self.cursor.execute("DELETE FROM kullanici WHERE okul_numarasi = ?", (okul_numarasi,))
                self.baglanti.commit()
        else:
            QtWidgets.QMessageBox.warning(self, 'Uyarı', 'Lütfen bir kayıt seçin!')

    def verileri_getir(self):
        self.tableWidget.setRowCount(0)
        self.cursor.execute("SELECT * FROM kullanici")
        veriler = self.cursor.fetchall()
        for satir_index, satir in enumerate(veriler):
            self.tableWidget.insertRow(satir_index)
            for sutun_index, sutun in enumerate(satir):
                self.tableWidget.setItem(satir_index, sutun_index, QTableWidgetItem(str(sutun)))

    def filtrele(self):
        secilen_sutun = self.comboBox_2.currentText()
        aranan_kelime = self.comboBox.currentText()

        if secilen_sutun == "Tümü":
            self.verileri_getir()
        else:
            self.cursor.execute("SELECT * FROM kullanici WHERE sinif = ?", (secilen_sutun,))
            veriler = self.cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for satir_index, satir in enumerate(veriler):
                self.tableWidget.insertRow(satir_index)
                for sutun_index, sutun in enumerate(satir):
                    self.tableWidget.setItem(satir_index, sutun_index, QTableWidgetItem(str(sutun)))


    def kayit_ara(self):
        aranan_kelime = self.lineEdit_5.text()
        self.cursor.execute("SELECT * FROM kullanici WHERE ad LIKE ? OR soyad LIKE ? OR okul_numarasi LIKE ? OR sinif LIKE ?",
                            ('%'+aranan_kelime+'%', '%'+aranan_kelime+'%', '%'+aranan_kelime+'%', '%'+aranan_kelime+'%'))
        veriler = self.cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for satir_index, satir in enumerate(veriler):
            self.tableWidget.insertRow(satir_index)
            for sutun_index, sutun in enumerate(satir):
                self.tableWidget.setItem(satir_index, sutun_index, QTableWidgetItem(str(sutun)))

    def temizle(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.verileri_getir()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
