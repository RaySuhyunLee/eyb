import sys
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QCursor
from PyQt4.QtCore import Qt
import usb

win = None

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)

        self.centralWidget = QtGui.QWidget(self)
        self.centralWidget.setGeometry(0, 0, 2000, 1500)

        self.centralWidget.setAutoFillBackground(True)
        p = self.centralWidget.palette()
        p.setColor(QtGui.QPalette.Window, QtGui.QColor(0, 0, 0))
        self.centralWidget.setPalette(p)
        
def on_press(is_on):
    if not is_on:
        win.hide()
        #QApplication.restoreOverrideCursor()
    else:
        win.showFullScreen()
        #QApplication.setOverrideCursor(Qt.WaitCursor)

if __name__ == "__main__":
    # start usb serial communication
    f = usb.scan()
    eyb = usb.connect(f[0])
    eyb.start_listen(on_press)

    app = QApplication(sys.argv)

    win = MyWindow()
    win.showFullScreen()

    app.exec_()

    eyb.stop_listen()
