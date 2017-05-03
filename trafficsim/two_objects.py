import sys, PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLCDNumber, QVBoxLayout, QSlider, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt5.QtGui import QIcon, QPen, QBrush, QColor, QPainter
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSignal, QObject


class Window(QMainWindow, QGraphicsView):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Proof of concept')
        self.setWindowIcon(QIcon('web.png'))
       # self.setGeometry(3000, 3000, 250, 150)
      #  vbox = QVBoxLayout()

      #  self.setLayout(vbox)
        self.initView()
        self.button = QPushButton('Test', self)
        self.button.move(50, 50)
        self.button.clicked.connect(self.myButtonClicked)

        self.statusBar()
        self.showMaximized()

    def myButtonClicked(self, event):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def initView(self):
        QGraphicsView.__init__(self)

        self.scene = QGraphicsScene()
        blueBrush =QBrush(QColor('blue'))
        outlinePen=QPen(QColor('black'))
        self.myRectt = QGraphicsRectItem(100, 30, 80, 100)

        self.myRectt.setBrush(blueBrush)
        self.myRectt.setPen(outlinePen)
        self.scene.addItem(self.myRectt)
        self.scene.setSceneRect(0, 0, 3000, 3000)

        self.myRect = QGraphicsRectItem(500, 200,80, 100)
        self.myRect.setBrush(blueBrush)
        self.myRect.setPen(outlinePen)
        self.scene.addItem(self.myRect)


        self.view = QGraphicsView(self.scene,self)
        self.view.resize(3000,3000)

    def keyPressEvent(self, e): # override !
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_W:
            self.statusBar().showMessage("UP pressed")
            self.myRectt.setY(self.myRectt.y()+1)
            self.show()
        elif e.key() == Qt.Key_D:
            self.statusBar().showMessage("RIGHT pressed")
            self.myRectt.setX(self.myRectt.x()+1)
            self.show()
        elif e.key() == Qt.Key_S:
            self.statusBar().showMessage("DOWN pressed")
            self.myRectt.setY(self.myRectt.y()-1)
            self.show()
        elif e.key() == Qt.Key_A:
            self.statusBar().showMessage("LEFT pressed")
            self.myRectt.setX(self.myRectt.x()-1)
        #    self.myRect.setPos(self.myRect.x(),self.myRect.y()-)
            self.show()


        elif e.key() == Qt.Key_8:
            self.statusBar().showMessage("UP pressed")
            self.myRect.setY(self.myRect.y()+1)
            self.show()
        elif e.key() == Qt.Key_6:
            self.statusBar().showMessage("RIGHT pressed")
            self.myRect.setX(self.myRect.x()+1)
            self.show()
        elif e.key() == Qt.Key_5:
            self.statusBar().showMessage("DOWN pressed")
            self.myRect.setY(self.myRect.y()-1)
            self.show()
        elif e.key() == Qt.Key_4:
            self.statusBar().showMessage("LEFT pressed")
            self.myRect.setX(self.myRect.x()-1)
        #    self.myRect.setPos(self.myRect.x(),self.myRect.y()-)
            self.show()

app = QApplication(sys.argv)
myWindow = Window()

sys.exit(app.exec_())
