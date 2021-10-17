from multiprocessing.pool import ThreadPool
from PyQt6 import QtCore
from currencies import currencies
from styles import styles
from PyQt6 import QtGui
from PyQt6.QtWidgets import (
    QComboBox,
    QMenu,
    QMainWindow,
    QMessageBox,
    QWidget,
    QApplication,
    QLineEdit,
    QTextEdit,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
    QHBoxLayout,
    QMainWindow,
)
import urllib.request as urllib2
import sys
import wx
import api
pool = ThreadPool(processes=2)
class UI_Window(QWidget):
    def __init__(self, parent=None):
        super(UI_Window, self).__init__(parent)
        self.home()
        

    def home(self):
        self.usd_trybutton = QPushButton("USD / TRY", self)
        self.aud_trybutton = QPushButton("AUD / TRY", self)
        self.eur_trybutton = QPushButton("EUR / TRY", self)
        self.cad_trybutton = QPushButton("CAD / TRY", self)
        self.gbp_trybutton = QPushButton("GBP / TRY", self)
        self.chf_trybutton = QPushButton("CHF / TRY", self)

        self.config_button_press()

        self.first_currency = QComboBox(self)
        self.second_currency = QComboBox(self)
        self.insert_currencies()
        self.amount_edittext = QLineEdit(self)
        self.calculate_button = QPushButton("Calculate",self)
        self.result = QLabel(self)
        
        self.result.setStyleSheet(styles.result_textview_style)

        self.first_currency.currentIndexChanged.connect(self.calculate)
        self.second_currency.currentIndexChanged.connect(self.calculate)
        self.amount_edittext.textChanged.connect(self.calculate)
        self.calculate_button.clicked.connect(self.calculate)

        self.onlyDouble = QtGui.QDoubleValidator()
        self.amount_edittext.setValidator(self.onlyDouble)
        self.amount_edittext.setPlaceholderText("Amount: ")
        self.amount_edittext.setMaxLength(8)

        self.first_currency.setStyleSheet(styles.currency_combobox_style)
        self.second_currency.setStyleSheet(styles.currency_combobox_style)
        self.amount_edittext.setStyleSheet(styles.amount_edittext_style)
        

        list = [self.usd_trybutton,self.aud_trybutton,self.eur_trybutton,self.cad_trybutton,self.gbp_trybutton,self.chf_trybutton]
        self.place_buttons(list)
        self.set_button_styles(list)
        returned_hbox = self.place_result_fragment()
        v_box = QVBoxLayout()
        v_box.addLayout(self.buttons_layout)
        v_box.addStretch()
        v_box.addLayout(returned_hbox)
        v_box.addStretch()
        self.setLayout(v_box)
    def insert_currencies(self):
        currency_list = currencies.get_currencies()
        self.first_currency.addItem("First Currency")
        self.first_currency.addItems(currency_list)
        self.second_currency.addItem("Second Currency")
        self.second_currency.addItems(currency_list)
    def config_button_press(self):
        self.usd_trybutton.clicked.connect(lambda: self.specific_button_pressed(self.usd_trybutton.text()))
        self.aud_trybutton.clicked.connect(lambda: self.specific_button_pressed(self.aud_trybutton.text()))
        self.eur_trybutton.clicked.connect(lambda: self.specific_button_pressed(self.eur_trybutton.text()))
        self.cad_trybutton.clicked.connect(lambda: self.specific_button_pressed(self.cad_trybutton.text()))
        self.gbp_trybutton.clicked.connect(lambda: self.specific_button_pressed(self.gbp_trybutton.text()))
        self.chf_trybutton.clicked.connect(lambda: self.specific_button_pressed(self.chf_trybutton.text()))

    def calculate(self,object):
        try:
            amount = str(self.amount_edittext.text())
            amount = float(amount)
            first_currency = self.first_currency.currentText()
            second_currency = self.second_currency.currentText()
            if(first_currency!="First Currency" and second_currency!="Second Currency"):
                value = api.get_data(first_currency,second_currency,amount)
                self.result.setText(f"{amount} {first_currency} = {value} {second_currency}")
        except:
            pass
    
    def place_result_fragment(self):
        h_box = QHBoxLayout()
        h_box.addWidget(self.first_currency)
        h_box.addWidget(self.amount_edittext)

        h_box1 = QHBoxLayout()
        h_box1.addWidget(self.second_currency)
        h_box1.addWidget(self.calculate_button)

        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.result)
        v_box = QVBoxLayout()

        v_box.addLayout(h_box)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)

        main_h_box = QHBoxLayout()
        main_h_box.addStretch()
        main_h_box.addLayout(v_box)
        main_h_box.addStretch()
        return main_h_box
    def place_buttons(self,list):
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addStretch()
        for i in list:
            self.buttons_layout.addWidget(i)
            self.buttons_layout.addStretch()
    def set_button_styles(self,list):
        for i in list:
            i.setStyleSheet(styles.specific_button_style)
    def specific_button_pressed(self, text):
        incoming_currency_list = text.split("/")
        self.first_currency.setCurrentText(str(incoming_currency_list[0][0:3]))
        self.second_currency.setCurrentText("TRY")
        self.amount_edittext.setText("1")
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        app = wx.App(False)

        self.width, self.height = wx.GetDisplaySize()
        self.setGeometry(
            round((self.width / 2) - 900), round((self.height / 2) - 500), 1200, 600
        )
        self.setWindowTitle("Anlık Döviz Verileri")
        self.setStyleSheet("background-color: rgba(255, 255, 255, .050);")
       
        self.startMainMenu()

    def startMainMenu(self):
        self.window = UI_Window(self)
        self.setWindowTitle("Anlık Döviz Verileri")
        self.setCentralWidget(self.window)
        self.showMaximized()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
