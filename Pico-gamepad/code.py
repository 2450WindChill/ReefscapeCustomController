# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# You must add a gamepad HID device inside your boot.py file
# in order to use this example.
# See this Learn Guide for details:
# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/hid-devices#custom-hid-devices-3096614-9

import board
import digitalio
import analogio
import usb_hid
import supervisor
import time
from digitalio import DigitalInOut, Direction, Pull
from hid_gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

upPin = board.GP4
upGamepad = 1

downPin = board.GP3
downGamepad = 2

bonk1Pin = board.GP5
bonk1Gamepad = 3

bonk2Pin = board.GP6
bonk2Gamepad = 4

HookPin = board.GP2
HookPinGamepad = 5
ActionLED = board.GP27

L1Pin = board.GP22
L1Gamepad = 6

L2LPin = board.GP20
L2LGamepad = 7

L2RPin = board.GP21
L2RGamepad = 8

L3LPin = board.GP18
L3LGamepad = 9

L3RPin = board.GP19
L3RGamepad = 10
ScoringLED = board.GP28

RF1Pin = board.GP7
RF1Gamepad = 11
RF1Led = board.GP12

RF2Pin = board.GP8
RF2Gamepad = 12
RF2Led = board.GP11

RF3Pin = board.GP17
RF3Gamepad = 13
RF3Led = board.GP15

RF4Pin = board.GP16
RF4Gamepad = 14
RF4Led = board.GP26

RF5Pin = board.GP9
RF5Gamepad = 15
RF5Led = board.GP14

RF6Pin = board.GP10
RF6Gamepad = 16
RF6Led = board.GP13



# Create some buttons. The physical buttons are connected
# to ground on one side and these and these pins on the other.
button_pins = ( upPin,
                downPin,
                bonk1Pin,
                bonk2Pin,
                HookPin,
                L1Pin,
                L2LPin,
                L2RPin,
                L3LPin,
                L3RPin,
                RF1Pin,
                RF2Pin,
                RF3Pin,
                RF4Pin,
                RF5Pin,
                RF6Pin )

# Map the buttons to button numbers on the Gamepad.
# gamepad_buttons[i] will send that button number when buttons[i]
# is pushed.
gamepad_buttons = ( upGamepad,
                    downGamepad,
                    bonk1Gamepad,
                    bonk2Gamepad,
                    HookPinGamepad,
                    L1Gamepad,
                    L2LGamepad,
                    L2RGamepad,
                    L3LGamepad,
                    L3RGamepad,
                    RF1Gamepad,
                    RF2Gamepad,
                    RF3Gamepad,
                    RF4Gamepad,
                    RF5Gamepad,
                    RF6Gamepad )

# The pins connected to each LED
ledpins = ( ActionLED,
           ScoringLED,
           RF1Led,
           RF2Led,
           RF3Led,
           RF4Led,
           RF5Led,
           RF6Led )

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

# Connect an analog two-axis joystick to A4 and A5.


# Equivalent of Arduino's map() function.
def range_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


leds = []

for pin in ledpins:
    led = DigitalInOut(pin)
    led.direction = Direction.OUTPUT
    leds.append(led)

# Action LEDS are always on, Scoring LEDS only turn on when at least one RF LED is on, RF LEDS turn on via networktables
leds[0].value = True
while True:
    if (leds[2].value == True) or (leds[3].value == True) or (leds[4].value == True) or (leds[5].value == True) or (leds[6].value == True) or (leds[7].value == True):
        leds[1].value = True
    else:
        leds[1].value = False

    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
        if value == "":
            continue
        print(value)
        if value == "RF1on":
            leds[2].value = True
        if value == "RF1off":
            leds[2].value = False

        if value == "RF2on":
            leds[3].value = True
        if value == "RF2off":
            leds[3].value = False

        if value == "RF3on":
            leds[4].value = True
        if value == "RF3off":
            leds[4].value = False

        if value == "RF4on":
            leds[5].value = True
        if value == "RF4off":
            leds[5].value = False
        
        if value == "RF5on":
            leds[6].value = True
        if value == "RF5off":
            leds[6].value = False
        
        if value == "RF6on":
            leds[7].value = True
        if value == "RF6off":
            leds[7].value = False

    # for led in range(len(ledpins)):
    #     switch_LED = leds[led]
    #     switch_LED.value = True
    #     time.sleep(1)
    #     switch_LED.value = False
    
    # Buttons are grounded when pressed (.value = False).
    for i, button in enumerate(buttons):
        gamepad_button_num = gamepad_buttons[i]
        if button.value:
            gp.release_buttons(gamepad_button_num)
            print(" release", gamepad_button_num, end="")
        else:
            gp.press_buttons(gamepad_button_num)
            print(" press", gamepad_button_num, end=""),
    
