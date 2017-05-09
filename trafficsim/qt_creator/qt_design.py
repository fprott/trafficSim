# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_design.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_qt_design(object):
    def setupUi(self, qt_design):
        qt_design.setObjectName("qt_design")
        qt_design.resize(955, 599)
        self.centralWidget = QtWidgets.QWidget(qt_design)
        self.centralWidget.setObjectName("centralWidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralWidget)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        qt_design.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(qt_design)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 955, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuDatei = QtWidgets.QMenu(self.menuBar)
        self.menuDatei.setObjectName("menuDatei")
        self.menuHilfe = QtWidgets.QMenu(self.menuBar)
        self.menuHilfe.setObjectName("menuHilfe")
        qt_design.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(qt_design)
        self.mainToolBar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainToolBar.setAcceptDrops(True)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        qt_design.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        qt_design.insertToolBarBreak(self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(qt_design)
        self.statusBar.setObjectName("statusBar")
        qt_design.setStatusBar(self.statusBar)
        self.actionDrawStreet = QtWidgets.QAction(qt_design)
        self.actionDrawStreet.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("qt_creator/icons/icon_road.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionDrawStreet.setIcon(icon)
        self.actionDrawStreet.setObjectName("actionDrawStreet")
        self.actionDeleteRoad = QtWidgets.QAction(qt_design)
        self.actionDeleteRoad.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("qt_creator/icons/icon_bulldozer.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionDeleteRoad.setIcon(icon1)
        self.actionDeleteRoad.setObjectName("actionDeleteRoad")
        self.action_ber_trafficSim = QtWidgets.QAction(qt_design)
        self.action_ber_trafficSim.setObjectName("action_ber_trafficSim")
        self.actionUrheberrecht_Informationen = QtWidgets.QAction(qt_design)
        self.actionUrheberrecht_Informationen.setObjectName("actionUrheberrecht_Informationen")
        self.menuHilfe.addAction(self.action_ber_trafficSim)
        self.menuHilfe.addAction(self.actionUrheberrecht_Informationen)
        self.menuBar.addAction(self.menuDatei.menuAction())
        self.menuBar.addAction(self.menuHilfe.menuAction())
        self.mainToolBar.addAction(self.actionDrawStreet)
        self.mainToolBar.addAction(self.actionDeleteRoad)

        self.retranslateUi(qt_design)
        QtCore.QMetaObject.connectSlotsByName(qt_design)

    def retranslateUi(self, qt_design):
        _translate = QtCore.QCoreApplication.translate
        qt_design.setWindowTitle(_translate("qt_design", "qt_design"))
        self.menuDatei.setTitle(_translate("qt_design", "Datei"))
        self.menuHilfe.setTitle(_translate("qt_design", "Hilfe"))
        self.actionDrawStreet.setText(_translate("qt_design", "Zeichne Straße"))
        self.actionDrawStreet.setToolTip(_translate("qt_design", "Setzen von Endpunkt der Straße"))
        self.actionDeleteRoad.setText(_translate("qt_design", "Lösche Straße"))
        self.actionDeleteRoad.setToolTip(_translate("qt_design", "Lösche einen Straßenpunkt"))
        self.action_ber_trafficSim.setText(_translate("qt_design", "Über trafficSim"))
        self.actionUrheberrecht_Informationen.setText(_translate("qt_design", "Urheberrecht Informationen"))

