import sys
import os
from PyQt4 import QtCore, QtGui
import usb

win = None

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.centralWidget = QtGui.QWidget(self)
        self.centralWidget.setGeometry(0, 0, 2000, 1500)
        
	self.pic = QtGui.QLabel(self.centralWidget)
	self.pic.setGeometry(0, 0, 2000, 1500)
	#use full ABSOLUTE path to the image, not relative
	self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/image.png"))

def on_press(is_pressed):
    if is_pressed:
        win.hide()
    else:
        win.showFullScreen()

if __name__ == "__main__":
    # start usb serial communication
    f = usb.scan()
    eyb = usb.connect(f[0])
    usb.start_listen(eyb, on_press)

    app = QtGui.QApplication(sys.argv)

    win = MyWindow()
    win.showFullScreen()

    app.exec_()

    usb.stop_listen()
