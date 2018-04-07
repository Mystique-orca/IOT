import RPi.GPIO as GPIO
import time
import datetime
import dht11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarning(False)
GPIO.cleanup()

instance=dht11.DHT11(pin=5)

while True:
    result=instance.read()
    if result.is_valid():
        print("Last valid input:"+ str(datetime.datetime.now()))
        print("Temperature:%d C" %result.temperature)
        print("Humidity:%d %%" %result.humidity)
    time.sleep(1)
