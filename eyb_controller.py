import sys
from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.setWindowTitle("Emergency!")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    win = MyWindow()
    win.showFullScreen()

    app.exec_()
