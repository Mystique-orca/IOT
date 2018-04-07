import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(15,GPIO.IN)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
while True:
    i=GPIO.input(15)
    time.sleep(0.2)
    if i==1:
        print("object is Detected",i) 
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        
    if i==0:
        print("Object is not detected",i)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        
