# Shifter class

import RPi.GPIO as GPIO
import time

class Shifter():

  'Shift register class'

  def __init__(self, data, latch, clock):
    self.dataPin, self.latchPin, self.clockPin = data, latch, clock
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.dataPin, GPIO.OUT) 
    GPIO.setup(self.latchPin, GPIO.OUT, initial=0)
    GPIO.setup(self.clockPin, GPIO.OUT, initial=0)

  def ping(self, pin):  # ping the clock or latch pin
    GPIO.output(pin,1)
    time.sleep(0)
    GPIO.output(pin,0)

  def shiftByte(self, byteVal):  # display a given byte pattern
    for i in range(8):           # 8 bits in register
      GPIO.output(self.dataPin, ~(byteVal & (1<<i)))  # if common anode
      #GPIO.output(self.dataPin, byteVal & (1<<i))    # if common cathode
      self.ping(self.clockPin)
    #self.ping(self.latchPin)

  def pingLatch(self):
    self.ping(self.latchPin)

pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

rows = [0b10000000, 0b01000000, 0b00100000, 0b00010000, 0b00001000, 0b00000100, 0b00000010, 0b00000001]


class LED8x8():


  pattern1 = [0b00000000]
  pattern2 = [0b11111111]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data,latch,clock)

  def display(self,num):
    global pattern
    global rows
    self.shifter.shiftByte(pattern[num])
    print(pattern[num])
    self.shifter.shiftByte(rows[num])
    print(rows[num]) #push first bite to second SR and send second byte
    self.shifter.pingLatch() #ping latch
    print("pinged latch")
    time.sleep(.001)
 


dataPin, latchPin, clockPin = 23, 24, 25

# Pick a number sequence


theLED8x8= LED8x8(dataPin, latchPin, clockPin)



while True:
  for n in range(8):
    theLED8x8.display(n)
    time.sleep(0.2)  
