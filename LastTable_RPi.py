from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LastWindow(object):
    def setupUilast(self, LastWin, YL, YR, L_mean, R_mean, L_median, R_median):
        LastWin.setObjectName("Dialog")
        LastWin.resize(325, 700)
        LastWin.move(1510, 62)
        LastWin.setWindowTitle("Hand asymmetry")
        LastWin.setWindowIcon(QtGui.QIcon("/home/pi/Desktop/Main/Bachelor/px_icon.png"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(LastWin)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(LastWin)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(YL) - 1)
        self.tableWidget.setHorizontalHeaderLabels(['LEFT HAND', 'RIGHT HAND', 'ASYMMETRY L~R (%)'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.verticalLayout.addWidget(self.tableWidget)
        self.str_general_asimmetria = QtWidgets.QLabel(LastWin)
        self.str_general_asimmetria.setMinimumSize(QtCore.QSize(305, 30))
        self.str_general_asimmetria.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setWeight(50)
        self.str_general_asimmetria.setFont(font)
        self.str_general_asimmetria.setObjectName("str_general_asimmetria")
        self.verticalLayout.addWidget(self.str_general_asimmetria)
        self.str_Zapazd_Operej = QtWidgets.QLabel(LastWin)
        self.str_Zapazd_Operej.setMinimumSize(QtCore.QSize(305, 80))
        self.str_Zapazd_Operej.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        self.str_Zapazd_Operej.setFont(font)
        self.str_Zapazd_Operej.setObjectName("str_Zapazd_Operej")
        self.verticalLayout.addWidget(self.str_Zapazd_Operej)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        YL = list(YL)
        YR = list(YR)

        del YL[0]
        del YR[0]

        gen_asm = 0
        for i in range(len(YL)):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(YL[i])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(YR[i])))
            asm = round(100 * (1 - (YL[i] / YR[i])), 1)
            asm = str(asm)
            if asm == '-inf': asm = '-100.0'
            gen_asm += float(asm)
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(asm))
        gen_asm = round(gen_asm, 1)
        if gen_asm < 0:
            self.str_general_asimmetria.setText(
                "Левая рука опережает правую руку на\n\t\t\t" + str(abs(gen_asm)) + " %")
        else:
            self.str_general_asimmetria.setText(
                "Правая рука опережает левую руку на\n\t\t\t" + str(abs(gen_asm)) + " %")
        if L_median > L_mean and R_median > R_mean:
            self.str_Zapazd_Operej.setText("ОПЕРЕЖЕНИЕ  левой руки на\t" + str(
                int(round((abs((L_median - L_mean) * 1000)), 3))) + " мс\nОПЕРЕЖЕНИЕ  правой руки на\t" + str(
                int(round((abs((R_median - R_mean) * 1000)), 3))) + " мс")
        if L_median < L_mean and R_median < R_mean:
            self.str_Zapazd_Operej.setText("ЗАПАЗДЫВАНИЕ  левой руки на\t" + str(
                int(round((abs((L_median - L_mean) * 1000)), 3))) + " мс\nЗАПАЗДЫВАНИЕ  правой руки на\t" + str(
                int(round((abs((R_median - R_mean) * 1000)), 3))) + " мс")
        if L_median < L_mean and R_median > R_mean:
            self.str_Zapazd_Operej.setText("ЗАПАЗДЫВАНИЕ  левой руки на\t" + str(
                int(round((abs((L_median - L_mean) * 1000)), 3))) + " мс\nОПЕРЕЖЕНИЕ  правой руки на\t" + str(
                int(round((abs((R_median - R_mean) * 1000)), 3))) + " мс")
        if L_median > L_mean and R_median < R_mean:
            self.str_Zapazd_Operej.setText("ОПЕРЕЖЕНИЕ  левой руки на\t" + str(
                int(round((abs((L_median - L_mean) * 1000)), 3))) + " мс\nЗАПАЗДЫВАНИЕ  правой руки на\t" + str(
                int(round((abs((R_median - R_mean) * 1000)), 3))) + " мс")
