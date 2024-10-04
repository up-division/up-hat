# Copyright (c) AAEON. All rights reserved.
# UP board ultrasonic HC-SR04 example
from periphery import GPIO
import sys
import time

if len(sys.argv) <= 2:
    print("usage:ultrasonic.py [trigger gpio] [echo gpio]")
    print("upboard gpio number 0~27")
    print("https://github.com/up-board/up-community/wiki/40Pin-Header")
    sys.exit()
    
trig=sys.argv[1]
echo=sys.argv[2]

# Open pin with input direction
gpio_echo = GPIO(int(echo),direction = "in")
# need to set in again, should be periphery's issue 
gpio_echo.direction = "in"
# Trigger gpio with output direction
gpio_trig = GPIO(int(trig),direction = "out")
gpio_trig.direction = "out"
try:  
    while True:
        # start
        counter=2000 #timeout counter
        gpio_trig.write(False)
        time.sleep(0.001)
        gpio_trig.write(True)
        time.sleep(0.01)
        gpio_trig.write(False)
        start_us=time.time_ns()/1000
        #wait for echo ping high
        while gpio_echo.read() != True :
            if counter == 0 :
                break;
            counter -= 1
            continue
        counter=2000
        start_us=time.time_ns()/1000
        #wait for echo ping low
        while gpio_echo.read() != False :
            if counter == 0 :
                break;
            counter -= 1
            continue
        end_us = time.time_ns()/1000
        cm = (end_us-start_us)/58
        print("%.2f cm" % cm)
        #inch=(end_us-start_us)/148
        #print("%.2f inch" % inch)
       
except KeyboardInterrupt:
    gpio_echo.close()
    gpio_trig.close()
    del gpio_echo
    del gpio_trig
    print("\nCtrl-c pressed.\n")
    
