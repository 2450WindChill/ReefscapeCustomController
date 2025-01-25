import serial
import time

ser = serial.Serial('COM4')
 # turns light on for 5 secs, shuts off after

 # sets data to 1, returns value
data = "1 \r\n"
print("Writing 1")
# writes data to controller, prints to terminal
print(ser.write(bytearray(data, 'ascii')))

time.sleep(5)

# sets data to 0, returns value
data = "0 \r\n"
print("Writing 0")
# writes data to controller, prints to terminal
print(ser.write(bytearray(data, 'ascii')))