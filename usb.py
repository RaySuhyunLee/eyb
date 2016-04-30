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
    device = serial.Serial(portInfo.device, 9600, timeout=.1)
    return Eyb(device)

class Eyb():
    def __init__(self, device):
        self.is_listen = False
        self.device = device

    def start_listen(self, callback):
        self.is_listen = True

        def listen(callback):
            while self.is_listen:
                data = self.device.readline()[:-2]
                if data == "on":
                    callback(True)
                    print("On!")
                elif data == "off":
                    callback(False)
                    print("Off!")

        self.th = threading.Thread(target=listen, args=(callback,))
        self.th.start()

    def stop_listen(self):
        self.is_listen = False
        self.th.join()
