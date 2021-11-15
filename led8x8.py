import time

from shifter import Shifter

dataPin, latchPin, clockPin = 23, 24, 25

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
    self.shifter.shiftByte(LED8x8.pattern[num])
   
    self.shifter.shiftByte(LED8x8.rows[num])

    self.shifter.pingLatch() #ping latch


    
    time.sleep(.001)
 
    
    
  
 