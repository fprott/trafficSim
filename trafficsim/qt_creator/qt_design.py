# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 541)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 711, 431))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 753, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuTrafficSim_GUI = QtWidgets.QMenu(self.menuBar)
        self.menuTrafficSim_GUI.setObjectName("menuTrafficSim_GUI")
        self.menuBearbeiten = QtWidgets.QMenu(self.menuBar)
        self.menuBearbeiten.setObjectName("menuBearbeiten")
        self.menuHilfe = QtWidgets.QMenu(self.menuBar)
        self.menuHilfe.setObjectName("menuHilfe")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_ber_TrafficSim = QtWidgets.QAction(MainWindow)
        self.action_ber_TrafficSim.setObjectName("action_ber_TrafficSim")
        self.menuHilfe.addAction(self.action_ber_TrafficSim)
        self.menuBar.addAction(self.menuTrafficSim_GUI.menuAction())
        self.menuBar.addAction(self.menuBearbeiten.menuAction())
        self.menuBar.addAction(self.menuHilfe.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuTrafficSim_GUI.setTitle(_translate("MainWindow", "Datei"))
        self.menuBearbeiten.setTitle(_translate("MainWindow", "Bearbeiten"))
        self.menuHilfe.setTitle(_translate("MainWindow", "Hilfe"))
        self.action_ber_TrafficSim.setText(_translate("MainWindow", "Über TrafficSim"))

