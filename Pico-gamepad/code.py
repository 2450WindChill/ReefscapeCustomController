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

RF1Pin = board.GP7
RF1Gamepad = 11

RF2Pin = board.GP8
RF2Gamepad = 12

RF3Pin = board.GP17
RF3Gamepad = 13

RF4Pin = board.GP16
RF4Gamepad = 14

RF5Pin = board.GP9
RF5Gamepad = 15

RF6Pin = board.GP10
RF6Gamepad = 16



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
                RF6Pin)

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
                    RF6Gamepad)

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

# Connect an analog two-axis joystick to A4 and A5.


# Equivalent of Arduino's map() function.
def range_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


while True:
    # Buttons are grounded when pressed (.value = False).
    for i, button in enumerate(buttons):
        gamepad_button_num = gamepad_buttons[i]
        if button.value:
            gp.release_buttons(gamepad_button_num)
            print(" release", gamepad_button_num, end="")
        else:
            gp.press_buttons(gamepad_button_num)
            print(" press", gamepad_button_num, end=""),
    
