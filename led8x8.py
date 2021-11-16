import time

from shifter import Shifter

dataPin, latchPin, clockPin = 23, 24, 25

rows = [0b10000000, 0b01000000, 0b00100000, 0b00010000, 0b00001000, 0b00000100, 0b00000010, 0b00000001]

pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001,
0b10100101, 0b10011001, 0b01000010, 0b00111100]

pattern1 = [0b00000000]
pattern2 = [0b11111111]

class LED8x8():



  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data,latch,clock)

  def display(self,num):
    global pattern1
    global pattern2
    global pattern
    global rows
    self.shifter.shiftByte(pattern2[num])
    self.shifter.shiftByte(pattern1[num])

    self.shifter.pingLatch() #ping latch
    
    time.sleep(.1)
 
    
    
  
 