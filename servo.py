import RPi.GPIO as GPIO
import time
import sys

servoPIN1 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN1, GPIO.OUT)
servoPIN2 = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN2, GPIO.OUT)

p1 = GPIO.PWM(servoPIN1, 50) # GPIO 17 for PWM with 50Hz
p2 = GPIO.PWM(servoPIN2, 50) # GPIO 17 for PWM with 50Hz
p1.start(0) # Initialization
p2.start(0) # Initialization
duty1 = int(sys.argv[1])
p1.ChangeDutyCycle(duty1)
duty2 = int(sys.argv[2])
p2.ChangeDutyCycle(duty2)
time.sleep(1)

p1.stop()
p2.stop()
GPIO.cleanup()
