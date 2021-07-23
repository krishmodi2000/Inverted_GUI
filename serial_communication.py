import serial
import time
import threading

data = None

def read_data():
    global data
    ser = serial.Serial('COM3', 9600, timeout = 1)
    while True:
        input = b'D'
        ser.write(input)

        data = ser.readline().decode('ascii')  #receive data
        time.sleep(10)

if __name__ == '__main__':
    t1 = threading.Thread(target=read_data)
    t1.start()

    while True:
        if data != None:
            print(data)
