import sys
import os
from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.centralWidget = QtGui.QWidget(self)
        self.centralWidget.setGeometry(0, 0, 2000, 1500)
        
	self.pic = QtGui.QLabel(self.centralWidget)
	self.pic.setGeometry(0, 0, 2000, 1500)
	#use full ABSOLUTE path to the image, not relative
	self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/image.png"))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    win = MyWindow()
    win.showFullScreen()

    app.exec_()
