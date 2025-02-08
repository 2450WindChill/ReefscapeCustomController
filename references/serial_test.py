import serial
import time

ser = serial.Serial('COM16')
 # turns light on for 5 secs, shuts off after

#  # sets data to 1, returns value
# data = "RF1on \r\n"
# print("Writing RF1on")
# # writes data to controller, prints to terminal
# print(ser.write(bytearray(data, 'ascii')))

# time.sleep(5)

# # sets data to 0, returns value
# data = "RF1off \r\n"
# print("Writing RF1off")
# # writes data to controller, prints to terminal
# print(ser.write(bytearray(data, 'ascii')))

# goes through each RF and turns on the LED, and then goes to a nonexistent RF to turn everything off for one round
while True:
    x = 1
    while x <= 7:
        data = "RF" + str(x) + "on \r\n"
        print(str(x) + " on")
        print(ser.write(bytearray(data, 'ascii')))

        time.sleep(2)

        data = "RF" + str(x) + "off \r\n"
        print(str(x) + " off")
        print(ser.write(bytearray(data, 'ascii')))

        x += 1