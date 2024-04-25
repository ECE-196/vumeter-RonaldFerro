# Write your code here :-)

import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26,  # type: ignore
    board.IO47,
    board.IO33,  # type: ignore
    board.IO34,  # type: ignore
    board.IO48,  # type: ignore
    board.IO35,  # type: ignore
    board.IO36,  # type: ignore
    board.IO37,  # type: ignore
    board.IO38,  # type: ignore
    board.IO39,  # type: ignore
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

minim = 0
maxim = 28000
step = (maxim - minim) / len(led_pins)

# main loop
while True:
    volume = microphone.value
    pinset = max(volume-20000, 0) // step
    print(volume)

    for a in range (0, len(leds)):
        leds[a].value = False


    for a in range (0, pinset):
        leds[a].value = True

