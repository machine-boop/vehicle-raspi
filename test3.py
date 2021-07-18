import time,RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.out)
GPIO.setup(25,GPIO.out)
GPIO.output(24,GPIO.HIGH)

