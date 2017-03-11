#  ___   ___  ___  _   _  ___   ___   ____ ___  ____  
# / _ \ /___)/ _ \| | | |/ _ \ / _ \ / ___) _ \|    \ 
#| |_| |___ | |_| | |_| | |_| | |_| ( (__| |_| | | | |
# \___/(___/ \___/ \__  |\___/ \___(_)____)___/|_|_|_|
#                  (____/ 
# 
#Project tutorial URL http://osoyoo.com/?p=774
#Copyright Osoyoo.com

import RPi.GPIO as GPIO
import time

#led_pin defines the pin number connected to LED 
led_pin = 40
count=10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

# flashing 10 times
for i in range(count):
    GPIO.output(led_pin,True)
    time.sleep(1)
    GPIO.output(led_pin,False)
    time.sleep(1)
GPIO.cleanup()