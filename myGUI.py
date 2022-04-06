from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
import PySide6
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 677)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(628, 403))
        MainWindow.setStyleSheet("background-color: #660066;\n"
"color: white;\n"
"font: 12pt \"verdana\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.code_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.code_Btn.setGeometry(QtCore.QRect(60, 590, 181, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.code_Btn.sizePolicy().hasHeightForWidth())
        self.code_Btn.setSizePolicy(sizePolicy)
        self.code_Btn.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: #a000a0;\n"
"\n"
"")
        self.code_Btn.setObjectName("code_Btn")
        self.decode_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.decode_Btn.setGeometry(QtCore.QRect(390, 590, 181, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decode_Btn.sizePolicy().hasHeightForWidth())
        self.decode_Btn.setSizePolicy(sizePolicy)
        self.decode_Btn.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: #a000a0;")
        self.decode_Btn.setObjectName("decode_Btn")
        self.entry_text = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_text.setGeometry(QtCore.QRect(20, 400, 261, 24))
        self.entry_text.setStyleSheet("border-radius:5px;\n"
"border:2px solid white;")
        self.entry_text.setObjectName("entry_text")
        self.reg = QtWidgets.QLineEdit(self.centralwidget)
        self.reg.setGeometry(QtCore.QRect(110, 230, 401, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reg.sizePolicy().hasHeightForWidth())
        self.reg.setSizePolicy(sizePolicy)
        self.reg.setStyleSheet("border-radius:5px;\n"
"border:2px solid white;")
        self.reg.setObjectName("reg")
        self.coded_text = QtWidgets.QLineEdit(self.centralwidget)
        self.coded_text.setGeometry(QtCore.QRect(350, 400, 261, 24))
        self.coded_text.setStyleSheet("border-radius:5px;\n"
"border:2px solid white;")
        self.coded_text.setObjectName("coded_text")
        self.entry_label = QtWidgets.QLabel(self.centralwidget)
        self.entry_label.setGeometry(QtCore.QRect(70, 340, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_label.sizePolicy().hasHeightForWidth())
        self.entry_label.setSizePolicy(sizePolicy)
        self.entry_label.setStyleSheet("border:2px solid black;\n"
"border-radius:10px;\n"
"background-color:#9966CC;\n"
"")
        self.entry_label.setObjectName("entry_label")
        self.coded_label = QtWidgets.QLabel(self.centralwidget)
        self.coded_label.setGeometry(QtCore.QRect(410, 340, 141, 41))
        self.coded_label.setStyleSheet("border:2px solid black;\n"
"border-radius:10px;\n"
"background-color:#9966CC;")
        self.coded_label.setObjectName("coded_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 170, 321, 41))
        self.label.setStyleSheet("border:2px solid black;\n"
"border-radius:10px;\n"
"background-color:#9966CC;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 221, 41))
        self.label_2.setStyleSheet("border-bottom: 2px solid black\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 80, 501, 41))
        self.label_3.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: #a000a0;\n"
"")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def code_text(self):
        import numpy as np

        try:

            def text_bin(text, encoding="utf-8", errors="surrogatepass"):
                bits = bin(int.from_bytes(text.encode(encoding, errors), "big"))[2:]
                return bits.zfill(8 * ((len(bits) + 7) // 8))

            print("CODE___________________")
            entry_text = self.entry_text.text()
            print(entry_text)
            entry_text = text_bin(entry_text)
            print(entry_text)
            n_sum = self.sum_count.value()
            summator = []
            reg = self.reg.text()
            reg = reg + " "
            mid_summator = []
            print(len(reg))
            for j in range(len(reg)):
                if reg[j].isdigit():
                    if int(reg[j]) > 3:
                        exit()
                    mid_summator.append(int(reg[j]))
                if reg[j] == " ":
                    summator.append(mid_summator)
                    mid_summator = []
            print("______sum__________")
            print(summator)
            print("______splitted_text__________")
            coded_sum = []
            for i in range(len(entry_text)):
                coded_sum.append(int(entry_text[i]))
            print(coded_sum)
            print("_______i(x)_________")
            ix = np.poly1d(coded_sum)
            print(ix)
            coded_sum = []
            for j in range(len(summator)):
                a = [0, 0, 0]
                for i in range(len(summator[j])):
                    a[summator[j][i] - 1] = 1
                coded_sum.append(a)
            gx = []
            for i in range(len(coded_sum)):
                gx.append(np.poly1d(coded_sum[i]))
                print("_______g" + str(i + 1) + "(x)_________")
                print(np.poly1d(coded_sum[i]))

            cx = []
            for i in range(len(gx)):
                cx.append(ix * gx[i])
            f = []
            for i in range(len(cx)):
                for j in range(len(cx[i])):
                    if cx[i][j] % 2 == 0:
                        cx[i][j] = 0
                    else:
                        cx[i][j] = 1
                print("______c" + str(i + 1) + "(x)__________")
                print(cx[i])
                f.append(np.asarray(cx[i].coef, list).tolist())
            print("_______coef_________")

            c = 0
            for i in range(len(f)):
                if c < len(f[i]):
                    c = len(f[i])
            print("max = ", c)
            for i in range(len(f)):
                f[i] = f[i][::-1]
                print(len(f[i]))
                while len(f[i]) < c:
                    f[i].append(0)
            print(f)
            pol = []
            for i in range(len(f)):
                if len(pol) < len(f[i]):
                    pol = f[i]
            f.remove(pol)
            if len(f) > 0:
                for i in range(len(f)):
                    for j in range(len(f[i])):
                        pol[j] = str(pol[j]) + str(f[i][j])
            print("____eq____")
            print(pol)
            coded_text = ""
            for i in range(len(pol)):
                coded_text = coded_text + pol[i]
            print("____coded_____")
            print(coded_text)
            self.coded_text.setText(coded_text)
            print(len(entry_text))
            print(len(coded_text))
            print("____decoded_____")
            dec_pol = [coded_text[i:i + len(coded_sum)] for i in range(0, len(coded_text), len(coded_sum))]
            print(dec_pol)
            dec_willy = []
            for i in range(len(dec_pol)):
                dec_willy.append(int(dec_pol[i][0]))
            dec_willy = dec_willy[::-1]
            dec_willy = np.poly1d(dec_willy)
            dec_willy = np.polydiv(dec_willy, gx[0])
            print(dec_willy[0])
            f = []
            strok = ""
            f = np.asarray(dec_willy[0].coef, list).tolist()
            for i in range(len(f)):
                f[i] = str(f[i])
                f[i] = f[i].replace(".0", "")
                f[i] = f[i].replace("-", "")
                if int(f[i]) % 2 == 0:
                    f[i] = "0"
                else:
                    f[i] = "1"
            for i in range(len(f)):
                strok = strok + str(f[i])
            print(strok)

            def textf(bits, encoding='utf-8', errors='surrogatepass'):
                n = int(bits, 2)
                return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

            print(textf(strok))

        except:
            self.coded_text.setText("Что-то не так!")

    def decode_text(self):

        import numpy as np

        try:

            print("DECODE___________________")

            coded_text = self.coded_text.text()
            n_sum = self.sum_count.value()
            print(coded_text)

            summator = []
            reg = self.reg.text()
            reg = reg + " "
            mid_summator = []
            for j in range(len(reg)):
                if reg[j].isdigit():
                    if int(reg[j]) > 3:
                        exit()
                    mid_summator.append(int(reg[j]))
                if reg[j] == " ":
                    summator.append(mid_summator)
                    mid_summator = []
            print("______sum__________")
            print(summator)
            coded_sum = []
            for j in range(len(summator)):
                a = [0, 0, 0]
                for i in range(len(summator[j])):
                    a[summator[j][i] - 1] = 1
                coded_sum.append(a)
            gx = []
            for i in range(len(coded_sum)):
                gx.append(np.poly1d(coded_sum[i]))
                print("_______g" + str(i + 1) + "(x)_________")
                print(np.poly1d(coded_sum[i]))

            dec_pol = [coded_text[i:i + len(coded_sum)] for i in range(0, len(coded_text), len(coded_sum))]
            print(dec_pol)
            dec_willy = []
            for i in range(len(dec_pol)):
                dec_willy.append(int(dec_pol[i][0]))
            dec_willy = dec_willy[::-1]
            dec_willy = np.poly1d(dec_willy)
            dec_willy = np.polydiv(dec_willy, gx[0])
            print("____i(x)_____")
            print(dec_willy[0])
            f = []
            strok = ""
            f = np.asarray(dec_willy[0].coef, list).tolist()
            for i in range(len(f)):
                f[i] = str(f[i])
                f[i] = f[i].replace(".0", "")
                f[i] = f[i].replace("-", "")
                if int(f[i]) % 2 == 0:
                    f[i] = "0"
                else:
                    f[i] = "1"
            for i in range(len(f)):
                strok = strok + str(f[i])
            print("____coded_len____")
            print(strok)

            def textf(bits, encoding='utf-8', errors='surrogatepass'):
                n = int(bits, 2)
                return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

            print("____decoded_word____")
            print(textf(strok))
            self.entry_text.setText(textf(strok))

        except:

            self.entry_text.setText("Что-то не так!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.code_Btn.setText(_translate("MainWindow", "Закодировать"))
        self.code_Btn.clicked.connect(self.code_text)
        self.decode_Btn.setText(_translate("MainWindow", "Декодировать"))
        self.decode_Btn.clicked.connect(self.decode_text)
        self.entry_label.setText(_translate("MainWindow", "Поле для текста"))
        self.coded_label.setText(_translate("MainWindow", "Поле для кода"))
        self.label.setText(_translate("MainWindow", "Количество сумматоров и регистров"))
        self.label_2.setText(_translate("MainWindow", "Лабораторная работа №2 "))
        self.label_3.setText(_translate("MainWindow", "Самый модный в мире кодер и декодер сверточного кода"))

from myGUI import Ui_MainWindow
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())