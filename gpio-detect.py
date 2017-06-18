# Tony Cheng <tony.pig@gmail.com>
# Version : 0.0.3
# Licensed under the Apache License, Version 2.0

import time, sys
import RPi.GPIO as GPIO

if (len(sys.argv)) != 2 :
    print('Argument error!\n Syntax: python gpio-detect.py <GPIO #>')
    print('Example: python gpio-detect.py 29')
    exit()

gpio_port = int(sys.argv[1])

GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_port, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def action(pin):
    print('Sensor detected action!')
    return

GPIO.add_event_detect(gpio_port, GPIO.RISING)
GPIO.add_event_callback(gpio_port, action)

try:
    while True:
        print('alive')
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
