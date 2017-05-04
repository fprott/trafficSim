# quick and dirty pyQT5 proof of concept
"""
GUI with PyQT5

GUI to build and test the system.

TODO:
    * EVERYTHING !
"""
import sys
import numpy
from qt_design import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui



class QTDesignWidget(QtWidgets.QMainWindow, Ui_MainWindow):



    def __init__(self, parent=None):
        super(QTDesignWidget, self).__init__(parent)

        self.setupUi(self)
        scene = QtWidgets.QGraphicsScene(self)

        self.myPixmap = QtGui.QPixmap(self.mapDrawing_graphicsView.size().width()-self.mapDrawing_graphicsView.pos().x(), self.mapDrawing_graphicsView.size().height()-self.mapDrawing_graphicsView.pos().y())


    #    self.myPixmap = QtGui.QPixmap(100,100)
    #    self.myPixmap.setDevicePixelRatio(0.2)
        self.myPixmap.fill(QtGui.QColor('black'))




        self.DriveMatrix = numpy.zeros((100, 100))
        scene.addPixmap(self.myPixmap)
        self.mapDrawing_graphicsView.setScene(scene)
     #   self.drawingMatrix = [[0 for x in range(self.mapDrawing_graphicsView.width())] for y in range(self.mapDrawing_graphicsView.height())]
        #i want to merge I REALLY WANT TO XD


    def mousePressEvent(self, event):
        max_x= self.mapDrawing_graphicsView.size().width()-self.mapDrawing_graphicsView.pos().x()
        max_y=self.mapDrawing_graphicsView.size().height()-self.mapDrawing_graphicsView.pos().y()
        self.DriveMatrix[int(100*(event.pos().x()-self.mapDrawing_graphicsView.pos().x())/max_x)][int(100*(event.pos().y()-self.mapDrawing_graphicsView.pos().y())/max_y)]=1

        myImage = self.myPixmap.toImage()
        myImage.setPixel((event.pos().x()-self.mapDrawing_graphicsView.pos().x()),(event.pos().y()-self.mapDrawing_graphicsView.pos().y()),255)
        myImage.setPixel((event.pos().x() - self.mapDrawing_graphicsView.pos().x()+1),
                                         (event.pos().y() - self.mapDrawing_graphicsView.pos().y()+1), 255)
        myImage.setPixel((event.pos().x() - self.mapDrawing_graphicsView.pos().x()+2),
                                         (event.pos().y() - self.mapDrawing_graphicsView.pos().y()+2), 255)
        myImage.setPixel((event.pos().x() - self.mapDrawing_graphicsView.pos().x()+3),
                                         (event.pos().y() - self.mapDrawing_graphicsView.pos().y()+3), 255)
        myImage.setPixel((event.pos().x() - self.mapDrawing_graphicsView.pos().x()+4),
                                         (event.pos().y() - self.mapDrawing_graphicsView.pos().y()+4), 255)
        self.myPixmap= myImage.toPixmap()

        #print('PRESSED : ', event.pos())

def main():
    """
    Main method to build and maintain the GUI Window

    This method should be called only once to start the GUI.
    Do NOT call this method twice!

    Args:

    Returns:

    Raises:
        KeyError:

    TODO:
        * Test it
    """
#    myMainWindow = Ui_MainWindow()
#    myMainWindow.setupUi()
    app = QtWidgets.QApplication(sys.argv)
    form = QTDesignWidget()
    form.show()
    app.exec_()

if __name__ == '__main__': #this will call the main if this file is called as main
    main()
