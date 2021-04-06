
# blink the given pin at 1Hz 50% duty cycle
# use ctrl-c to end

# notify
print('LOAD: blinker.py')

import time
from machine import Pin

def blink(pin=5):
    p = Pin(pin,Pin.OUT)
    try:
          while True:
            p.value(0)
            print('pin',pin,'ON')
            time.sleep_ms(500)
            p.value(1)
            print('pin',pin,'OFF')
            time.sleep_ms(500)
    except:
        p.value(1)
        Pin(pin,Pin.IN)
