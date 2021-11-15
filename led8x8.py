import time

from shifter import Shifter

dataPin, latchPin, clockPin = 23, 24, 25




class LED8x8():

  #pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]
  pattern1 = [0b00000000]
  pattern2 = [0b11111111]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data,latch,clock)

  def display(self):
    self.shifter.shiftByte(LED8x8.pattern2[0])
    self.shifter.shiftByte(LED8x8.pattern1[0]) #send second byte
    self.shifter.pingLatch()
 
    
    
  
 