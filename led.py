import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

while True:
    GPIO.output(3,True)
    GPIO.output(5,False)
    GPIO.output(11,True)
    GPIO.output(13,False)
    time.sleep(0.2)
    print('LED 3 ON')
    GPIO.output(3,False)
    GPIO.output(5,True)
    GPIO.output(11,False)
    GPIO.output(13,True)
    time.sleep(0.2)
    print('LED 2 ON')
   
   
    
  

        
