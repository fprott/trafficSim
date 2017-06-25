# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_design_neu.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,QTime)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
                             QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
                             QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #tab_Strasse
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 771, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Strasse = QtWidgets.QWidget()
        self.tab_Strasse.setObjectName("tab_Strasse")

        self.frame_Strasse = QtWidgets.QFrame(self.tab_Strasse)
        self.frame_Strasse.setGeometry(QtCore.QRect(10, 10, 500, 500))
        self.frame_Strasse.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Strasse.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Strasse.setObjectName("frame_Strasse")
        """
        self.lable_1 = QtWidgets.QLabel(self.frame_Strasse)
        self.lable_1.setGeometry((QtCore.QRect(0,0,500,500)))
        self.lable_1.setText("Hallo World")
        self.lable_1.setPixmap(QtGui.QPixmap("qt_creator\icons\Background.png"))
        self.lable_1.setObjectName("Background")
        """
        self.pushButton_Add_Strasse = QtWidgets.QPushButton(self.tab_Strasse)
        self.pushButton_Add_Strasse.setGeometry(QtCore.QRect(520, 10, 80, 23))
        self.pushButton_Add_Strasse.setObjectName("pushButton_Add_Strasse")
        self.pushButton_Add_Strasse.setCheckable(True)

        self.pushButton_Losen_Strasse = QtWidgets.QPushButton(self.tab_Strasse)
        self.pushButton_Losen_Strasse.setGeometry(QtCore.QRect(620, 10, 80, 23))
        self.pushButton_Losen_Strasse.setObjectName("pushButton_Losen_Strasse")
        self.pushButton_Losen_Strasse.setCheckable(True)

        self.lineEdit_Str_Bereite = QtWidgets.QLineEdit(self.tab_Strasse)
        self.lineEdit_Str_Bereite.setGeometry(QtCore.QRect(720, 10, 30, 23))
        self.lineEdit_Str_Bereite.setObjectName("lineEdit_Str_Bereite")

        self.lineEdit_Str_Punkte = QtWidgets.QLineEdit(self.tab_Strasse)
        self.lineEdit_Str_Punkte.setGeometry(QtCore.QRect(620, 490, 130, 23))
        self.lineEdit_Str_Punkte.setObjectName("lineEdit_Str_Punkte")

        self.treeView_Strasse = QtWidgets.QTreeWidget(self.tab_Strasse)     #Tree Widget in Strasse_Tab
        self.treeView_Strasse.setGeometry(QtCore.QRect(520, 40, 231, 441))
        self.treeView_Strasse.setObjectName("treeView_Strasse")
        self.treeView_Strasse.setColumnCount(2)
        self.treeView_Strasse.setHeaderLabels(["Strasse","Points"])

        root = QtWidgets.QTreeWidgetItem(self.treeView_Strasse)
        root.setText(0, 'root')
        root.setSelected(True)
        child1 = QtWidgets.QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, 'name1')
        child2 = QtWidgets.QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, 'name2')
        child3 = QtWidgets.QTreeWidgetItem(root)
        child3.setText(0, 'child3')
        child4 = QtWidgets.QTreeWidgetItem(child3)
        child4.setText(0, 'child4')
        child4.setText(1, 'name4')
        self.treeView_Strasse.setCurrentItem(root)
        print(self.treeView_Strasse.selectedItems())
        #self.treeView_Strasse.removeItemWidget(self.treeView_Strasse.takeTopLevelItem(2))#self.treeView_Strasse.selectedItems())

        self.pushButton_Speichen_Strasse = QtWidgets.QPushButton(self.tab_Strasse)
        self.pushButton_Speichen_Strasse.setGeometry(QtCore.QRect(520, 490, 75, 23))
        self.pushButton_Speichen_Strasse.setObjectName("pushButton_Speichen_Strasse")

        self.tabWidget.addTab(self.tab_Strasse, "")

        #tab_Fahrzeug
        self.tab_Fahrzeug = QtWidgets.QWidget()
        self.tab_Fahrzeug.setObjectName("tab_Fahrzeug")

        self.frame_Fahrzeug = QtWidgets.QFrame(self.tab_Fahrzeug)
        self.frame_Fahrzeug.setGeometry(QtCore.QRect(10, 10, 500, 500))
        self.frame_Fahrzeug.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Fahrzeug.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Fahrzeug.setObjectName("frame_Fahrzeug")

        self.comboBox_Fahrzeug = QtWidgets.QComboBox(self.tab_Fahrzeug)
        self.comboBox_Fahrzeug.setGeometry(QtCore.QRect(520, 10, 171, 22))
        self.comboBox_Fahrzeug.setObjectName("comboBox_Fahrzeug")
        self.comboBox_Fahrzeug.insertItem(0,"Blue Car")
        self.comboBox_Fahrzeug.insertItem(1,"Black Car")
        self.comboBox_Fahrzeug.insertItem(2,"Green Car")
        self.comboBox_Fahrzeug.insertItem(3,"Purpur Car")
        self.comboBox_Fahrzeug.insertItem(4,"Red Car")
        self.comboBox_Fahrzeug.insertItem(5,"White Car")
        self.comboBox_Fahrzeug.insertItem(6,"Yellow Bus")
        self.comboBox_Fahrzeug.insertItem(7,"White Bus")

        self.pushButton_Add_Fahrzeug = QtWidgets.QPushButton(self.tab_Fahrzeug)
        self.pushButton_Add_Fahrzeug.setGeometry(QtCore.QRect(700, 10, 21, 23))
        self.pushButton_Add_Fahrzeug.setObjectName("pushButton_Add_Fahrzeug")
        self.pushButton_Add_Fahrzeug.setCheckable(True)

        self.pushButton_Losen_Fahrzeug = QtWidgets.QPushButton(self.tab_Fahrzeug)
        self.pushButton_Losen_Fahrzeug.setGeometry(QtCore.QRect(730, 10, 21, 23))
        self.pushButton_Losen_Fahrzeug.setObjectName("pushButton_Losen_Fahrzeug")

        self.treeView_Fahrzeug = QtWidgets.QTreeWidget(self.tab_Fahrzeug)     #Tree Widget in Strasse_Tab
        self.treeView_Fahrzeug.setGeometry(QtCore.QRect(520, 40, 231, 441))
        self.treeView_Fahrzeug.setObjectName("treeView_Fahrzeug")
        self.treeView_Fahrzeug.setColumnCount(2)
        self.treeView_Fahrzeug.setHeaderLabels(["Fahrzeug","Points"])

        self.lineEdit_Fahrzeug_Punkte = QtWidgets.QLineEdit(self.tab_Fahrzeug)
        self.lineEdit_Fahrzeug_Punkte.setGeometry(QtCore.QRect(620, 490, 130, 23))
        self.lineEdit_Fahrzeug_Punkte.setObjectName("lineEdit_Fahrzeug_Punkte")

        self.pushButton_Speichen_Fahrzeug = QtWidgets.QPushButton(self.tab_Fahrzeug)
        self.pushButton_Speichen_Fahrzeug.setGeometry(QtCore.QRect(520, 490, 75, 23))
        self.pushButton_Speichen_Fahrzeug.setObjectName("pushButton_Speichen_Fahrzeug")
        self.tabWidget.addTab(self.tab_Fahrzeug, "")

        #tab_Simulation
        self.tab_Simulation = QtWidgets.QWidget()
        self.tab_Simulation.setObjectName("tab_Simulation")

        self.frame_Simulation = QtWidgets.QFrame(self.tab_Simulation)
        self.frame_Simulation.setGeometry(QtCore.QRect(10, 10, 500, 500))
        self.frame_Simulation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Simulation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Simulation.setObjectName("frame_Simulation")

        self.horizontalSlider_Simulation = QtWidgets.QSlider(self.tab_Simulation)
        self.horizontalSlider_Simulation.setGeometry(QtCore.QRect(10, 520, 741, 22))
        self.horizontalSlider_Simulation.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Simulation.setObjectName("horizontalSlider_Simulation")
        self.horizontalSlider_Simulation.setRange(0,230)
        self.horizontalSlider_Simulation.setValue(1)
        self.horizontalSlider_Simulation.setTracking(True)

        self.lineEdit_Str_Doku_Simulation = QtWidgets.QLineEdit(self.tab_Simulation)
        self.lineEdit_Str_Doku_Simulation.setGeometry(QtCore.QRect(520, 30, 201, 20))
        self.lineEdit_Str_Doku_Simulation.setObjectName("lineEdit_Str_Doku_Simulation")

        self.label_Str_Doku_Simulation = QtWidgets.QLabel(self.tab_Simulation)
        self.label_Str_Doku_Simulation.setGeometry(QtCore.QRect(520, 10, 101, 16))
        self.label_Str_Doku_Simulation.setObjectName("label_Str_Doku_Simulation")

        self.lineEdit_FZ_Doku_Simulation = QtWidgets.QLineEdit(self.tab_Simulation)
        self.lineEdit_FZ_Doku_Simulation.setGeometry(QtCore.QRect(520, 70, 201, 20))
        self.lineEdit_FZ_Doku_Simulation.setObjectName("lineEdit_FZ_Doku_Simulation")

        self.label_FZ_Doku_Simulation = QtWidgets.QLabel(self.tab_Simulation)
        self.label_FZ_Doku_Simulation.setGeometry(QtCore.QRect(520, 50, 111, 16))
        self.label_FZ_Doku_Simulation.setObjectName("label_FZ_Doku_Simulation")

        self.toolButton_Str_Doku_Simulation = QtWidgets.QToolButton(self.tab_Simulation)
        self.toolButton_Str_Doku_Simulation.setGeometry(QtCore.QRect(730, 30, 25, 19))
        self.toolButton_Str_Doku_Simulation.setObjectName("toolButton_Str_Doku_Simulation")
        self.toolButton_FZ_Doku_Simulation = QtWidgets.QToolButton(self.tab_Simulation)
        self.toolButton_FZ_Doku_Simulation.setGeometry(QtCore.QRect(730, 70, 25, 19))
        self.toolButton_FZ_Doku_Simulation.setObjectName("toolButton_FZ_Doku_Simulation")

        self.label_GM_Simulation = QtWidgets.QLabel(self.tab_Simulation)
        self.label_GM_Simulation.setGeometry(QtCore.QRect(520, 90, 61, 16))
        self.label_GM_Simulation.setObjectName("label_GM_Simulation")

        self.comboBox_Gutemasse_Simulation = QtWidgets.QComboBox(self.tab_Simulation)
        self.comboBox_Gutemasse_Simulation.setGeometry(QtCore.QRect(520, 110, 231, 22))
        self.comboBox_Gutemasse_Simulation.setObjectName("comboBox_Gutemasse_Simulation")
        self.comboBox_Gutemasse_Simulation.insertItem(0,"Zeit Optimal")
        self.comboBox_Gutemasse_Simulation.insertItem(1,"Energie Optimal")

        self.pushButton_Start_Simulation = QtWidgets.QPushButton(self.tab_Simulation)
        self.pushButton_Start_Simulation.setGeometry(QtCore.QRect(580, 490, 75, 23))
        self.pushButton_Start_Simulation.setObjectName("pushButton_Start_Simulation")
        self.pushButton_Stop_Simulation = QtWidgets.QPushButton(self.tab_Simulation)
        self.pushButton_Stop_Simulation.setGeometry(QtCore.QRect(670, 490, 75, 23))
        self.pushButton_Stop_Simulation.setObjectName("pushButton_Stop_Simulation")

        self.listWidget_Simulation = QtWidgets.QListWidget(self.tab_Simulation)
        self.listWidget_Simulation.setGeometry(QtCore.QRect(520, 140, 231, 341))
        self.listWidget_Simulation.setObjectName("listWidget_Simulation")
        self.tabWidget.addTab(self.tab_Simulation, "")

        #MainWindow
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Datei = QtWidgets.QMenu(self.menubar)
        self.menu_Datei.setObjectName("menu_Datei")
        self.menu_Hilfe = QtWidgets.QMenu(self.menubar)
        self.menu_Hilfe.setObjectName("menu_Hilfe")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_Urheberrecht_Informationen = QtWidgets.QAction(MainWindow)
        self.action_Urheberrecht_Informationen.setObjectName("action_Urheberrecht_Informationen")
        self.action_uber_Traffic_Sim = QtWidgets.QAction(MainWindow)
        self.action_uber_Traffic_Sim.setObjectName("action_uber_Traffic_Sim")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.menu_Datei.addAction(self.action_Exit)
        self.menu_Hilfe.addAction(self.action_uber_Traffic_Sim)
        self.menu_Hilfe.addAction(self.action_Urheberrecht_Informationen)
        self.menubar.addAction(self.menu_Datei.menuAction())
        self.menubar.addAction(self.menu_Hilfe.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_Add_Strasse.setText(_translate("MainWindow", "Add Strasse"))
        self.pushButton_Losen_Strasse.setText(_translate("MainWindow", "Lösen Strasse"))
        self.lineEdit_Str_Bereite.setText(_translate("MainWindow", "20"))
        self.pushButton_Speichen_Strasse.setText(_translate("MainWindow", "Speichen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Strasse), _translate("MainWindow", "Straße"))
        self.pushButton_Add_Fahrzeug.setText(_translate("MainWindow", "+"))
        self.pushButton_Losen_Fahrzeug.setText(_translate("MainWindow", "-"))
        self.pushButton_Speichen_Fahrzeug.setText(_translate("MainWindow", "Speichen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Fahrzeug), _translate("MainWindow", "Fahrzeug"))
        self.label_Str_Doku_Simulation.setText(_translate("MainWindow", "Straßen Dokumente"))
        self.label_FZ_Doku_Simulation.setText(_translate("MainWindow", "Fahrzeuge Dokumente"))
        self.toolButton_Str_Doku_Simulation.setText(_translate("MainWindow", "..."))
        self.toolButton_FZ_Doku_Simulation.setText(_translate("MainWindow", "..."))
        self.label_GM_Simulation.setText(_translate("MainWindow", "Gütemaße"))
        self.pushButton_Start_Simulation.setText(_translate("MainWindow", "Start"))
        self.pushButton_Stop_Simulation.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Simulation), _translate("MainWindow", "Simulation"))
        self.menu_Datei.setTitle(_translate("MainWindow", "Datei"))
        self.menu_Hilfe.setTitle(_translate("MainWindow", "Hilfe"))
        self.action_Urheberrecht_Informationen.setText(_translate("MainWindow", "Urheberrecht Informationen"))
        self.action_uber_Traffic_Sim.setText(_translate("MainWindow", "Über Traffic_Sim"))
        self.action_Exit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

