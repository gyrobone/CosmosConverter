import sys
from PyQt5 import QtGui, QtWidgets, QtCore

class ConvertWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ConvertWindow, self).__init__()
        self.setGeometry(50,50,200,150)
        self.setWindowTitle("Distance Converter")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.home()

    def home(self):
        button = QtWidgets.QPushButton("Quit", self)
        button.clicked.connect(lambda: sys.exit())
        button.resize(button.sizeHint())
        button.move(0,0)

        self.textbox = QtWidgets.QLineEdit(self)
        self.textbox.move(10, 35)
        self.textbox.resize(120, 35)

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.addItem("Miles")
        self.comboBox.addItem("Kilometers")
        self.comboBox.addItem("Lightyears")
        self.comboBox.addItem("AU")
        self.comboBox.addItem("Parsecs")
        self.comboBox.addItem("Kiloparsecs")
        self.comboBox.move(5, 75)

        button = QtWidgets.QPushButton("Calculate", self)
        button.clicked.connect(lambda: self.get_args())
        button.resize(button.sizeHint())
        button.move(0, 100)

        self.show()

    def get_args(self):
        try:
            number = int(self.textbox.text())
        except ValueError:
            print("Please Enter A Number")
        unit = self.comboBox.currentText().lower()
        ConvertWindow.convert(number, unit)

    def result(self, text):
        w = QtWidgets.QWidget
        label = QtWidgets.QLabel(w)
        label.setText(text)
        w.show()

    def miles_to_km(miles):
        try:
            m = int(miles)
        except ValueError:
            print("Please Type Number")
            return
        km = m * 1.60934
        text = "Kilometers: ~" + str(km)
        print(text)

    def km_to_au(kilometers):
        try:
            km = int(kilometers)
        except ValueError:
            print("Please Type Number")
            return
        au = km * 6.68459e-9
        text = "Astronomical Units: ~" + str(au)
        print(text)

    def au_to_ly(astro_units):
        try:
            au = int(astro_units)
        except ValueError:
            print("Please Type Number")
            return
        ly = au * 1.5813e-5
        text = "Lightyears: ~" + str(ly)
        print(text)

    def ly_to_au(lightyears):
        try:
            ly = int(lightyears)
        except ValueError:
            print("Please Type Number")
            return
        au = ly * 63241.1
        text = "Astronomical Units: ~" + str(au)
        print(text)

    def ly_to_pc(lightyears):
        try:
            ly = int(lightyears)
        except ValueError:
            print("Please Type Number")
            return
        pc = ly * 0.306601
        text = "Parsecs: ~" + str(pc)
        print(text)

    def pc_to_kpc(parsecs):
        try:
            pc = int(parsecs)
        except ValueError:
            print("Please Type Number")
            return
        kpc = pc * 0.001
        text = "Kiloparsecs: ~" + str(kpc)
        print(text)

    def kpc_to_Mpc(kiloparsecs):
        try:
            kpc = int(kiloparsecs)
        except ValueError:
            print("Please Type Number")
            return
        Mpc = kpc * 0.001
        text = "Megaparsecs: ~" + str(Mpc)
        print(text)

    def convert(number, unit):
        try:
            n = int(number)
        except ValueError:
            print("Please Type Number")
            return
        if unit == "miles":
            ConvertWindow.miles_to_km(n)
        elif unit == "kilometers":
            ConvertWindow.km_to_au(n)
        elif unit == "au":
            ConvertWindow.au_to_ly(n)
        elif unit == "lightyears":
            ConvertWindow.ly_to_pc(n)
            ConvertWindow.ly_to_au(n)
        elif unit == "parsecs":
            ConvertWindow.pc_to_kpc(n)
        elif unit == "kiloparsecs":
            ConvertWindow.kpc_to_Mpc(n)
        else:
            print("Please Enter Valid Unit")

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = ConvertWindow()
    sys.exit(app.exec_())

run()