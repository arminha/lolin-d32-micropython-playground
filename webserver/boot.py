# This file is executed on every boot (including wake-boot from deepsleep)

from machine import Pin
import network
import gc
import esp
esp.osdebug(None)

def connect_wifi(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)

    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print('Connection successful')
    print(station.ifconfig())

gc.collect()

ssid = 'REPLACE_WITH_YOUR_SSID'
password = 'replace_with_your_password'

connect_wifi(ssid, password)

led = Pin(5, Pin.OUT)
