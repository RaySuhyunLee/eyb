import serial
from serial.tools import list_ports
import threading

def scan():
    dev_list = list_ports.comports()
    filtered = []
    for dev in dev_list:
        print(dev.product)
        if dev.product and ("usb" in dev.product or "USB" in dev.product):
            filtered.append(dev)

    return filtered

def connect(portInfo):
    eyb = serial.Serial(portInfo.device, 9600, timeout=.1)
    return eyb

is_listen = False

def start_listen(eyb, callback):
    is_listen = True
    def listen(eyb, callback):
        while is_listen:
            data = eyb.readline()[:-2]
            if data == "on":
                #callback(True)
                print("On!")
            elif data == "off":
                #callback(False)
                print("Off!")

    th = threading.Thread(target=listen, args=(eyb, callback,))
    th.start()

def stop_listen():
    is_listen = False

