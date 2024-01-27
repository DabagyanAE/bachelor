from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import statistics as st
import math
import seaborn as sns
import numpy as np
import scipy
from scipy import interpolate

def plot_single_empty_graph(Left, Right):
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(100, 70), dpi=100, facecolor='white', frameon=False,
                             edgecolor='black', linewidth=1)
    fig.subplots_adjust(wspace=0.4, hspace=0.6, left=0.05, right=0.97, top=0.98, bottom=0.05)
    axes.grid(True, c='lightgrey', alpha=0.3)

    w = Calculations()
    LLCor, RRCor, LLm, RRm = w.correct_miss(Left, Right)
    LL_mean, RR_mean, LL_stdev, RR_stdev, LL_var, RR_var, LL_median, RR_median, LL_razmax, RR_razmax = w.statist(LLCor, RRCor)

    interval = (max(LLCor + RRCor) - min(LLCor + RRCor)) / (math.ceil(math.sqrt((len(LLCor) + len(RRCor)) / 2)))
    if len(LLCor) > len(RRCor):
        kolvo = math.ceil(math.sqrt(len(LLCor)))
    else:
        kolvo = math.ceil(math.sqrt(len(RRCor)))
    if kolvo < 8:
        kolvo = 8

    x = [(min(LLCor + RRCor) - interval)]
    xx = [x[0] - interval / 2]
    for i in range(kolvo + 2):
        x.append(min(LLCor + RRCor) + (i * interval))
        xx.append((min(LLCor + RRCor) + (i * interval)) - interval / 2)

    YLL, bnsl, pl = axes.hist(LLCor, bins=x, stacked=True, color="blue", alpha=0.5, label="Левая рука", align="mid")
    YRR, bnsr, pr = axes.hist(RRCor, bins=x, stacked=True, color="red", alpha=0.5, label="Правая рука", align="mid")

    del xx[0]

    xnew = np.linspace(min(xx), max(xx), 100)
    fff_L = interpolate.make_interp_spline(xnew, scipy.stats.norm.pdf(xnew, LL_mean, LL_stdev), k=3)
    fff_R = interpolate.make_interp_spline(xnew, scipy.stats.norm.pdf(xnew, RR_mean, RR_stdev), k=3)
    ynew_L = fff_L(xnew)
    ynew_R = fff_R(xnew)

    axes.plot(xnew, ynew_L, c='blue', lw=3, label='Левая рука')
    axes.plot(xnew, ynew_R, c='red', lw=3, label='Правая рука')

    axes.legend(loc='upper right')

    return fig, YLL, YRR

class Calculations():
    def correct_miss(self, left, right):
        self.left = left
        self.right = right
        LL_correct = []
        LL_miss = []
        RR_correct = []
        RR_miss = []
        for i in range(len(self.left)):
            if self.left[i] < st.mean(self.left) + (3 * st.stdev(self.left)) and self.left[i] > st.mean(self.left) - (3 * st.stdev(self.left)):
                LL_correct.append(self.left[i])
            else:
                LL_miss.append(self.left[i])
        for i in range(len(self.right)):
            if self.right[i] < st.mean(self.right) + (3 * st.stdev(self.right)) and self.right[i] > st.mean(self.right) - (3 * st.stdev(self.right)):
                RR_correct.append(self.right[i])
            else:
                RR_miss.append(self.right[i])

        return LL_correct, RR_correct, LL_miss, RR_miss

    def statist(self, Leftc, Rightc):
        L_mean = st.mean(Leftc)
        R_mean = st.mean(Rightc)
        L_stdev = st.stdev(Leftc)
        R_stdev = st.stdev(Rightc)
        L_var = st.variance(Leftc)
        R_var = st.variance(Rightc)
        L_median = st.median(Leftc)
        R_median = st.median(Rightc)
        L_razmax = max(Leftc) - min(Leftc)
        R_razmax = max(Rightc) - min(Rightc)

        return L_mean, R_mean, L_stdev, R_stdev, L_var, R_var, L_median, R_median, L_razmax, R_razmax

class MyMplCanvas(FigureCanvas):
    def __init__(self, fig, parent=None):
        self.fig = fig
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

class Ui_Conclusion(object):
    def setupconclUi(self, ConclMain, Left, Right):
        ConclMain.setObjectName("Dialog")
        ConclMain.resize(1400, 900)
        ConclMain.move(110, 62)
        ConclMain.setWindowTitle("Conclusion")
        ConclMain.setWindowIcon(QtGui.QIcon("/home/pi/Desktop/Main/Bachelor/px_icon.png"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(ConclMain)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InitDataTable = QtWidgets.QTableWidget(ConclMain)
        self.InitDataTable.setObjectName("InitDataTable")
        self.InitDataTable.setColumnCount(2)
        self.InitDataTable.setRowCount(100)
        self.InitDataTable.setMinimumSize(250, 500)
        self.InitDataTable.setMaximumWidth(250)
        self.InitDataTable.verticalHeader().setVisible(True)
        self.InitDataTable.setHorizontalHeaderLabels(['ЛЕВАЯ РУКА', 'ПРАВАЯ РУКА'])

        errL = 0
        errR = 0
        for i in range(len(Left)):
            if Left[i] == 'Error':
                del Left[i]
                errL += 1
        for i in range(len(Right)):
            if Right[i] == 'Error':
                del Right[i]
                errR += 1

        for i in range(len(Left)):
            self.InitDataTable.setItem(i, 0, QtWidgets.QTableWidgetItem(str(Left[i])))
            self.InitDataTable.setItem(i, 1, QtWidgets.QTableWidgetItem(str(Right[i])))

        self.horizontalLayout.addWidget(self.InitDataTable)
        self.MplWidget = QtWidgets.QWidget(ConclMain)
        self.MplWidget.setObjectName("MplWidget")
        self.MplWidget.setMinimumSize(500, 500)
        self.MplWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.fig, YLLLLL, YRRRRR = plot_single_empty_graph(Left, Right)

        w = Calculations()
        LLCor, RRCor, LLm, RRm = w.correct_miss(Left, Right)
        L_mean, R_mean, L_stdev, R_stdev, L_var, R_var, L_median, R_median, L_razmax, R_razmax = w.statist(LLCor, RRCor)

        self.companovka_for_mpl = QtWidgets.QVBoxLayout(self.MplWidget)
        self.canvas = MyMplCanvas(self.fig)
        self.companovka_for_mpl.addWidget(self.canvas)

        self.horizontalLayout.addWidget(self.MplWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.str_Sigma = QtWidgets.QLabel(ConclMain)
        self.str_Sigma.setMinimumSize(QtCore.QSize(0, 100))
        self.str_Sigma.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Arial black")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        self.str_Sigma.setFont(font)
        self.str_Sigma.setObjectName("str_Sigma")
        self.str_Sigma.setText("СТАНДАРТНОЕ ОТКЛОНЕНИЕ\n\nЛевая рука \t= " + str(
            round(L_stdev, 5)) + "\nПравая рука\t= " + str(round(R_stdev, 5)))
        self.verticalLayout.addWidget(self.str_Sigma)
        self.str_Mean = QtWidgets.QLabel(ConclMain)
        self.str_Mean.setMinimumSize(QtCore.QSize(0, 100))
        self.str_Mean.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        self.str_Mean.setFont(font)
        self.str_Mean.setObjectName("str_Matojidanie")
        self.str_Mean.setText("МАТЕМАТИЧЕСКОЕ ОЖИДАНИЕ\n\nЛевая рука \t= " + str(
            round(L_mean, 3)) + "\nПравая рука\t= " + str(round(R_mean, 3)))
        self.verticalLayout.addWidget(self.str_Mean)
        self.str_Dispersia = QtWidgets.QLabel(ConclMain)
        self.str_Dispersia.setMinimumSize(QtCore.QSize(0, 100))
        self.str_Dispersia.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        self.str_Dispersia.setFont(font)
        self.str_Dispersia.setObjectName("str_Dispersia")
        self.str_Dispersia.setText("ДИСПЕРСИЯ\n\nЛевая рука \t= " + str(
            round(L_var, 6)) + "\nПравая рука\t= " + str(round(R_var, 6)))
        self.verticalLayout.addWidget(self.str_Dispersia)
        self.str_Mediana = QtWidgets.QLabel(ConclMain)
        self.str_Mediana.setMinimumSize(QtCore.QSize(0, 100))
        self.str_Mediana.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        self.str_Mediana.setFont(font)
        self.str_Mediana.setObjectName("str_Mediana")
        self.str_Mediana.setText("МЕДИАНА\n\nЛевая рука \t= " + str(
            round(L_median, 3)) + "\nПравая рука\t= " + str(round(R_median, 3)))
        self.verticalLayout.addWidget(self.str_Mediana)
        self.str_Oshibki = QtWidgets.QLabel(ConclMain)
        self.str_Oshibki.setMinimumSize(QtCore.QSize(0, 100))
        self.str_Oshibki.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        self.str_Oshibki.setFont(font)
        self.str_Oshibki.setObjectName("str_Oshibki")
        self.str_Oshibki.setText("КОЛИЧЕСТВО ОШИБОК\n\nЛевая рука \t= " + str(
            errL) + "\nПравая рука\t= " + str(errR))
        self.verticalLayout.addWidget(self.str_Oshibki)
        self.str_Otsev = QtWidgets.QLabel(ConclMain)
        self.str_Otsev.setMinimumSize(QtCore.QSize(0, 100))
        self.str_Otsev.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        self.str_Otsev.setFont(font)
        self.str_Otsev.setObjectName("str_Otsev")
        self.str_Otsev.setText("КОЛИЧЕСТВО ОТСЕЯННЫХ ТОЧЕК\n\nЛевая рука \t= " + str(
            len(LLm)) + "\nПравая рука\t= " + str(len(RRm)))
        self.verticalLayout.addWidget(self.str_Otsev)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        return YLLLLL, YRRRRR, L_mean, R_mean, L_median, R_median
