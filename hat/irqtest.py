# UP board irq example for python
# interrupt handle using poll() in user space
from periphery import GPIO
import sys

if len(sys.argv) <= 1 or len(sys.argv) >29:
    print("usage:irqtest.py [gpio number]")
    print("upboard gpio number 0~27")
    sys.exit()

gpios=[]    
for i in sys.argv:
  gpios.append(i)
del gpios[0]

for k in gpios:
  if int(k) > 27 or int(k) < 0:
    print("invalid input")
    print("upboard gpio number 0~27")
    sys.exit()
    
print("IRQ testing gpio",gpios)

# Open pin with input direction
gpios_irq=[]
for n in gpios:
    gpios_irq.append(GPIO(int(n),direction = "in"))
    
# need to set in again, should be periphery's issue 
for x in gpios_irq:
    x.direction = "in"
    x.edge = "both"

try:  
    while True:
        irqs = GPIO.poll_multiple(gpios_irq)
        for irq in irqs:
            val = irq.read()
            if val==0:
                print("falling", irq.line)
            else:
                print("rising", irq.line)
                
except KeyboardInterrupt:
    del gpios_irq
    print("\nCtrl-c pressed.\n")
