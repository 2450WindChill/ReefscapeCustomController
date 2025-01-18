#!/usr/bin/env python3
#
# This is a NetworkTables client (eg, the DriverStation/coprocessor side).
# You need to tell it the IP address of the NetworkTables server (the
# robot or simulator).
#
# When running, this will continue incrementing the value 'dsTime', and the
# value should be visible to other networktables clients and the robot.
#

import sys
import time
from networktables import NetworkTables
import serial

# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    exit(0)

ip = sys.argv[1]
print(ip)

NetworkTables.initialize(server=ip)

sd = NetworkTables.getTable("SmartDashboard")

i = 0
while True:

    # gets and sets the limit switches into s1 and s2
    s1 = sd.getBoolean("SwitchOne", False)
    s2 = sd.getBoolean("SwitchTwo", False)

    # prints out values of s1 and s2 every 0.5s
    print("switchOne:", str(s1))
    print("switchTwo:", str(s2))
    print("---------------")
    time.sleep(0.5)

    #print("robotTime:", sd.getNumber("robotTime", -1))

    #sd.putNumber("dsTime", i)
    #time.sleep(1)
    #i += 1
