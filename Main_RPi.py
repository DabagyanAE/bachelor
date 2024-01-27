import sys, time, random, threading
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
from Conclusion_RPi import Ui_Conclusion
from LastTable_RPi import Ui_LastWindow

KeyPinL = 17
KeyPinR = 27

LEFT_HAND = []
RIGHT_HAND = []

GPIO.setmode(GPIO.BCM)
GPIO.setup(KeyPinL, GPIO.IN)
GPIO.setup(KeyPinR, GPIO.IN)

choise_OBJECT = {'Черный круг': '/home/pi/Desktop/Main/Bachelor/px_circle.png',
                 'Мяч': '/home/pi/Desktop/Main/Bachelor/px_ball01.png'}

choise_FON = {'Сплошной цвет': '/home/pi/Desktop/Main/Bachelor/px_green.png',
              'Трава': '/home/pi/Desktop/Main/Bachelor/px_grass.jpg'}

class Ui_Menu(object):
    def setupUi(self, Ui_Menu):
        Ui_Menu.setObjectName("MainWindow")
        Ui_Menu.resize(320, 580)
        Ui_Menu.move(800, 187)
        Ui_Menu.setWindowIcon(QtGui.QIcon("/home/pi/Desktop/Main/Bachelor/px_icon.png"))
        Ui_Menu.setMaximumSize(320, 580)
        Ui_Menu.setMinimumSize(320, 580)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Ui_Menu.setFont(font)
        Ui_Menu.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Ui_Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setObjectName("gridLayout_1")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem, 15, 8, 1, 1)
        self.DLIT_POYAV_OBJ = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DLIT_POYAV_OBJ.setFont(font)
        self.DLIT_POYAV_OBJ.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.DLIT_POYAV_OBJ.setAlignment(QtCore.Qt.AlignCenter)
        self.DLIT_POYAV_OBJ.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.DLIT_POYAV_OBJ.setObjectName("DLIT_POYAV_OBJ")
        self.gridLayout_1.addWidget(self.DLIT_POYAV_OBJ, 6, 0, 1, 9)
        self.INTER_POYAV = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.INTER_POYAV.setFont(font)
        self.INTER_POYAV.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.INTER_POYAV.setAlignment(QtCore.Qt.AlignCenter)
        self.INTER_POYAV.setObjectName("INTER_POYAV")
        self.gridLayout_1.addWidget(self.INTER_POYAV, 10, 0, 1, 9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_1.addItem(spacerItem1, 15, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem2, 15, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_1.addItem(spacerItem3, 13, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem4, 11, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem5, 15, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem6, 15, 3, 1, 1)
        self.DLIT_TEST = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DLIT_TEST.setFont(font)
        self.DLIT_TEST.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.DLIT_TEST.setAlignment(QtCore.Qt.AlignCenter)
        self.DLIT_TEST.setObjectName("DLIT_TEST")
        self.gridLayout_1.addWidget(self.DLIT_TEST, 3, 0, 1, 9)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem7, 15, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem8, 15, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_1.addItem(spacerItem9, 2, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_1.addItem(spacerItem10, 14, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_1.addItem(spacerItem11, 1, 4, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem12, 15, 7, 1, 1)
        self.btn_NEXT = QtWidgets.QPushButton(self.centralwidget)
        self.btn_NEXT.setEnabled(True)
        self.btn_NEXT.setGeometry(QtCore.QRect(30, 480, 260, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_NEXT.setFont(font)
        self.btn_NEXT.setIconSize(QtCore.QSize(16, 16))
        self.btn_NEXT.setShortcut("")
        self.btn_NEXT.setCheckable(False)
        self.btn_NEXT.setAutoDefault(False)
        self.btn_NEXT.setDefault(True)
        self.btn_NEXT.setFlat(False)
        self.btn_NEXT.setObjectName("btn_NEXT")
        self.str_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.str_1.setFont(font)
        self.str_1.setMouseTracking(True)
        self.str_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.str_1.setInputMask("")
        self.str_1.setFrame(True)
        self.str_1.setClearButtonEnabled(True)
        self.str_1.setObjectName("str_1")
        self.gridLayout_1.addWidget(self.str_1, 4, 4, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_1.addItem(spacerItem13, 5, 4, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_1.addItem(spacerItem14, 9, 4, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem15, 15, 6, 1, 1)
        self.str_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.str_2.setClearButtonEnabled(True)
        self.str_2.setObjectName("str_2")
        self.gridLayout_1.addWidget(self.str_2, 8, 4, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_1.addItem(spacerItem16, 11, 3, 1, 1)
        self.RAZ = QtWidgets.QLabel(self.centralwidget)
        self.RAZ.setGeometry(QtCore.QRect(240, 100, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.RAZ.setFont(font)
        self.RAZ.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.RAZ.setAlignment(QtCore.Qt.AlignCenter)
        self.RAZ.setObjectName("RAZ")
        self.SEC = QtWidgets.QLabel(self.centralwidget)
        self.SEC.setGeometry(QtCore.QRect(240, 190, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.SEC.setFont(font)
        self.SEC.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.SEC.setAlignment(QtCore.Qt.AlignCenter)
        self.SEC.setObjectName("SEC")
        self.MENU_NASTROEK = QtWidgets.QLabel(self.centralwidget)
        self.MENU_NASTROEK.setGeometry(QtCore.QRect(10, 30, 301, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MENU_NASTROEK.sizePolicy().hasHeightForWidth())
        self.MENU_NASTROEK.setSizePolicy(sizePolicy)
        self.MENU_NASTROEK.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.MENU_NASTROEK.setFont(font)
        self.MENU_NASTROEK.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.MENU_NASTROEK.setScaledContents(False)
        self.MENU_NASTROEK.setAlignment(QtCore.Qt.AlignCenter)
        self.MENU_NASTROEK.setWordWrap(False)
        self.MENU_NASTROEK.setObjectName("MENU_NASTROEK")
        self.SEC_2 = QtWidgets.QLabel(self.centralwidget)
        self.SEC_2.setGeometry(QtCore.QRect(130, 270, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.SEC_2.setFont(font)
        self.SEC_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.SEC_2.setAlignment(QtCore.Qt.AlignCenter)
        self.SEC_2.setObjectName("SEC_2")
        self.SEC_3 = QtWidgets.QLabel(self.centralwidget)
        self.SEC_3.setGeometry(QtCore.QRect(240, 270, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.SEC_3.setFont(font)
        self.SEC_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.SEC_3.setAlignment(QtCore.Qt.AlignCenter)
        self.SEC_3.setObjectName("SEC_3")
        self.str_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.str_3.setGeometry(QtCore.QRect(70, 270, 61, 21))
        self.str_3.setClearButtonEnabled(True)
        self.str_3.setObjectName("str_3")
        self.str_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.str_4.setGeometry(QtCore.QRect(180, 270, 61, 21))
        self.str_4.setClearButtonEnabled(True)
        self.str_4.setObjectName("str_4")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 320, 301, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.FON = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FON.setFont(font)
        self.FON.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.FON.setAlignment(QtCore.Qt.AlignCenter)
        self.FON.setObjectName("FON")
        self.gridLayout.addWidget(self.FON, 0, 0, 1, 1)
        self.OBJECT = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OBJECT.setFont(font)
        self.OBJECT.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.OBJECT.setAlignment(QtCore.Qt.AlignCenter)
        self.OBJECT.setObjectName("OBJECT")
        self.gridLayout.addWidget(self.OBJECT, 0, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem17, 2, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem18, 2, 1, 1, 1)
        self.comboBox_FON = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_FON.setObjectName("comboBox_FON")
        self.gridLayout.addWidget(self.comboBox_FON, 1, 0, 1, 1)
        self.comboBox_OBJECT = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_OBJECT.setEditable(False)
        self.comboBox_OBJECT.setCurrentText("")
        self.comboBox_OBJECT.setObjectName("comboBox_OBJECT")
        self.comboBox_OBJECT.addItems(choise_OBJECT)
        self.comboBox_FON.addItems(choise_FON)
        self.gridLayout.addWidget(self.comboBox_OBJECT, 1, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 400, 301, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem19, 2, 0, 1, 1)
        self.login = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.login.setAlignment(QtCore.Qt.AlignCenter)
        self.login.setObjectName("login")
        self.gridLayout_2.addWidget(self.login, 0, 0, 1, 1)
        self.str_login = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.str_login.setObjectName("str_login")
        self.gridLayout_2.addWidget(self.str_login, 1, 0, 1, 1)

        self.retranslateUi(Ui_Menu)
        QtCore.QMetaObject.connectSlotsByName(Ui_Menu)

    def retranslateUi(self, Ui_Menu):
        _translate = QtCore.QCoreApplication.translate
        Ui_Menu.setWindowTitle(_translate("MainWindow", "Menu"))
        self.DLIT_POYAV_OBJ.setText(_translate("MainWindow", "Длительность появления объекта"))
        self.INTER_POYAV.setText(_translate("MainWindow", "Интервалы появления"))
        self.DLIT_TEST.setText(_translate("MainWindow", "Длительность тестирования"))
        self.str_1.setText(_translate("MainWindow", "100"))
        self.str_2.setText(_translate("MainWindow", "1"))
        self.RAZ.setText(_translate("MainWindow", "раз"))
        self.SEC.setText(_translate("MainWindow", "сек"))
        self.btn_NEXT.setText(_translate("MainWindow", "START"))
        self.MENU_NASTROEK.setText(_translate("MainWindow", "МЕНЮ НАСТРОЕК"))
        self.SEC_2.setText(_translate("MainWindow", "сек"))
        self.SEC_3.setText(_translate("MainWindow", "сек"))
        self.str_3.setText(_translate("MainWindow", "1"))
        self.str_4.setText(_translate("MainWindow", "5"))
        self.FON.setText(_translate("MainWindow", "Фон"))
        self.OBJECT.setText(_translate("MainWindow", "Объект"))
        self.login.setText(_translate("MainWindow", "LOGIN"))
        self.str_login.setText(_translate("MainWindow", "Горохов Денис"))

class Communicate(QObject):
    closeApp = pyqtSignal()

class Ui_Secon(QtWidgets.QWidget):
    a = 0
    a1 = 1
    def setupUi2(self, Ui_Secon, objURL, fonUrl):
        Ui_Secon.setObjectName("Secondary")
        Ui_Secon.resize(800, 700)
        Ui_Secon.setWindowTitle("TESTING")
        Ui_Secon.setMinimumSize(800, 700)
        Ui_Secon.setMaximumSize(800, 700)
        Ui_Secon.move(560, 162)
        Ui_Secon.setWindowIcon(QtGui.QIcon("/home/pi/Desktop/Main/Bachelor/px_icon.png"))

        quit = QtWidgets.QAction("Quit", self)
        quit.triggered.connect(self.close)

        self.MainWindow = Ui_Secon
        self.grass = QtWidgets.QLabel(Ui_Secon)
        self.grass.setPixmap(QtGui.QPixmap(fonUrl))
        self.grass.setGeometry(QtCore.QRect(0, 0, 800, 700))
        self.grass.setAlignment(QtCore.Qt.AlignCenter)
        self.grass.setObjectName("pict_grass")
        self.grass.setVisible(True)  # Отображение ФОНА

        self.ball = QtWidgets.QLabel(Ui_Secon)
        self.ball.setPixmap(QtGui.QPixmap(objURL))
        self.ball.setObjectName("pict_ball")
        self.ball.setVisible(False)  # Отображение ОБЪЕКТА

        self.done = QtWidgets.QLabel(Ui_Secon)
        self.done.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Main/Bachelor/px_done_w.png"))
        self.done.setGeometry(0, 0, 800, 700)
        self.done.setAlignment(QtCore.Qt.AlignCenter)
        self.done.setObjectName("pict_done")
        self.done.setVisible(False)

        self.num1 = QtWidgets.QLabel(Ui_Secon)
        self.num1.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Main/Bachelor/px_1.png"))
        self.num1.setGeometry(0, 0, 800, 700)
        self.num1.setAlignment(QtCore.Qt.AlignCenter)
        self.num1.setObjectName("pict_num1")
        self.num1.setVisible(False)

        self.num2 = QtWidgets.QLabel(Ui_Secon)
        self.num2.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Main/Bachelor/px_2.png"))
        self.num2.setGeometry(0, 0, 800, 700)
        self.num2.setAlignment(QtCore.Qt.AlignCenter)
        self.num2.setObjectName("pict_num2")
        self.num2.setVisible(False)

        self.num3 = QtWidgets.QLabel(Ui_Secon)
        self.num3.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Main/Bachelor/px_3.png"))
        self.num3.setGeometry(0, 0, 800, 700)
        self.num3.setAlignment(QtCore.Qt.AlignCenter)
        self.num3.setObjectName("pict_num3")
        self.num3.setVisible(False)

        self.retranslateUi(Ui_Secon)
        QtCore.QMetaObject.connectSlotsByName(Ui_Secon)

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        threading.Timer(3, self.HideObj).start()

    def closeEvent(self, event):
        event.accept()
        self.c.closeApp.emit()

    def retranslateUi(self, Ui_Secon):
        _translate = QtCore.QCoreApplication.translate
        Ui_Secon.setWindowTitle(_translate("Ui_Secon", "TESTING"))

    def inputparam(self, x, y, z, b, login):
        self.ShowDelay = x  # Длительность появления объекта
        self.y = y          # Интервал ОТ
        self.z = z          # Интервал ДО
        self.b = b          # Длительность тестирования
        self.login = login  # ФИО

    def ShowObj(self):
        RR = False
        LL = False
        tm = time.monotonic()
        rr = tm + self.ShowDelay
        self.ball.setVisible(True)
        while True:
            try:
                S = time.monotonic()
                if S < rr:
                    if GPIO.input(KeyPinL) == False and LL == False:
                        reactL = time.monotonic() - tm
                        LL = True
                        LEFT_HAND.append(round(reactL, 5))
                    if GPIO.input(KeyPinR) == False and RR == False:
                        reactR = time.monotonic() - tm
                        RR = True
                        RIGHT_HAND.append(round(reactR, 5))
                else:
                    if LL == False:
                        LEFT_HAND.append('Error')
                    if RR == False:
                        RIGHT_HAND.append('Error')
                    self.HideObj()
                    break
            except KeyboardInterrupt:
                print('except')
                break

    def HideObj(self):
        while GPIO.input(KeyPinL) == False or GPIO.input(KeyPinR) == False:
            pass
        self.L_Error = False
        self.R_Error = False
        self.ball.setVisible(False)
        rr = random.uniform(self.y, self.z)         # Время Hide
        uu = time.monotonic() + rr                  # Время Hide + monotonic
        self.ball.setGeometry(random.randint(50, 650), random.randint(50, 550), 100, 100)
        if self.a != self.b:
            self.a += 1
            while True:
                    try:    # used try so that if user pressed other than the given key error will't be shown
                        H = time.monotonic()
                        if H < uu:
                            if GPIO.input(KeyPinL) == False:
                                uu = time.monotonic() + rr
                                if self.L_Error == False:
                                    self.L_Error = True
                                    LEFT_HAND.append('Error')
                            if GPIO.input(KeyPinR) == False:
                                uu = time.monotonic() + rr
                                if self.R_Error == False:
                                    self.R_Error = True
                                    RIGHT_HAND.append('Error')
                        else:
                            self.ShowObj()
                            break
                    except KeyboardInterrupt:
                        print('except')
                        break
        else:                           # Конец тестирования
            self.done.setVisible(True)
            self.data_output(LEFT_HAND, RIGHT_HAND)

    def closeWindow(self):
        self.close()

    def data_output(self, L, R):
        xxx = open('/home/pi/Desktop/Main/Bachelor\\' + self.login + '.txt', 'w')
        for index in range(self.b):
            xxx.write(str(L[index]) + '\t' + str(R[index]) + '\n')
        xxx.close()


class StartWindow(QtWidgets.QWidget, Ui_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_NEXT.clicked.connect(self.but_1)  # Нажатие на NEXT

    def but_1(self):
        self.inst = QtWidgets.QDialog()
        ui_ins = Ui_Secon()
        ui_ins.inputparam(float(self.str_2.text()), float(self.str_3.text()), float(self.str_4.text()),
                          int(self.str_1.text()), str(self.str_login.text()))
        cOB = choise_OBJECT[self.comboBox_OBJECT.currentText()]
        cFO = choise_FON[self.comboBox_FON.currentText()]
        ui_ins.setupUi2(self.inst, cOB, cFO)
        self.inst.setVisible(True)  # Отображение Secondary
        self.inst.exec()
        YL, YR, L_mean, R_mean, L_median, R_median = self.ConclWin()
        self.LastWin(YL, YR, L_mean, R_mean, L_median, R_median)

    def ConclWin(self):
        self.inst1 = QtWidgets.QDialog()
        win1 = ConclusionWindow()
        YLLLLLL, YRRRRRR, L_mean, R_mean, L_median, R_median = win1.setupconclUi(self.inst1, Left=LEFT_HAND, Right=RIGHT_HAND)
        self.inst1.setVisible(True)

        return YLLLLLL, YRRRRRR, L_mean, R_mean, L_median, R_median

    def LastWin(self, YLL, YRR, L_mean, R_mean, L_median, R_median):
        self.inst2 = QtWidgets.QDialog()
        win2 = Ui_LastWindow()
        win2.setupUilast(self.inst2, YLL, YRR, L_mean, R_mean, L_median, R_median)
        self.inst2.setVisible(True)

class ConclusionWindow(QtWidgets.QDialog, Ui_Conclusion):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupconclUi(self, LEFT_HAND, RIGHT_HAND)

class LastTableWindow(QtWidgets.QDialog, Ui_LastWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__()
        self.setupUilast(self)

if __name__ == '__main__':
    QApp = QtWidgets.QApplication(sys.argv)
    w = StartWindow()
    w.show()  # Отображение Menu
    sys.exit(QApp.exec())
