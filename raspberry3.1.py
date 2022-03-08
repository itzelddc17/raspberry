import re
import subprocess

host = 'jetbrains.com'
ping_output = subprocess.check_output(['ping','-c 5', host])

for line in ping_output.splitlines():
    print (line)

import RPi.GPIO as GPIO
import time
"""GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print ("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print ("LED off")
GPIO.output(18,GPIO.LOW)"""

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
pwm = GPIO.PWM(12,100)
print("\nPress Ctl C to quit \n")
dc = 0
pwm.start(dc)
try:
    while True:
        for dc in range(0, 101, 5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05)
            print(dc)
        for dc in range(95, 0, -5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05)
            print(dc)
except KeyboardInterrupt:
    print("Ctl C pressed - ending program")
pwm.stop()
GPIO.cleanup()
