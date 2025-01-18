import serial
import time

ser = serial.Serial('COM3')

data = 1
ser.write(data)
time.sleep(5)
data = 0
ser.write(data)