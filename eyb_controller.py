import sys
from PyQt4 import QtCore, QtGui

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    label = QtGui.QLabel("Hello, World!")
    label.show()
    label2 = QtGui.QLabel("Hello 2")
    label2.show()
    app.exec_()
