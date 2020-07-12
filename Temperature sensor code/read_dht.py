from dth import DTH
from machine import Pin
import time

# Type 0 = dht11
# Type 1 = dht22

def value():
    # I use pin 10 on my board hence the 'P10' and my sensor is a dth11 so the 0 in the end
    th = DTH(Pin('P10', mode=Pin.OPEN_DRAIN), 0)
    time.sleep(3)
    result = th.read()
    if result.is_valid():
        return(result.temperature,result.humidity)
