import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26,GPIO.IN)

ir_sensor =  GPIO.input(26)

def main():
  while True:
  
    if sensor ==  1:
      print("Line detected")
    
      else:
        print("Line not detected")
      
