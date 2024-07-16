# UP board irq example for python
# interrupt handle using poll() in user space
from periphery import GPIO
import sys

if len(sys.argv) <= 1:
    print("usage:irqtest.py [gpio number]")
    print("upboard gpio number 0~27")
    sys.exit()
    
gpio=sys.argv[1]
print("IRQ testing gpio",gpio)

# Open pin with input direction
gpio_irq = GPIO(int(gpio),direction = "in")
# need to set in again, should be periphery's issue 
gpio_irq.direction = "in"
gpio_irq.edge = "both"

try:  
    while True:
        ret = gpio_irq.poll()
        if ret==True:
            val = gpio_irq.read()
            if val==0:
                print("falling")
            else:
                print("rising")
                
except KeyboardInterrupt:
    gpio_irq.close()
    del gpio_irq
    print("\nCtrl-c pressed.\n")
    
