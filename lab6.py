import time
from led8x8 import LED8x8

# Simple demonstration of the LEDdisplay class.
# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins, since LEDdisplay is
# pin-agnostic).

dataPin, latchPin, clockPin = 23, 24, 25

# Pick a number sequence


theLED8x8= LED8x8(dataPin, latchPin, clockPin)



while True:
  theLED8x8.display(0,0)
  time.sleep(0.001)  

