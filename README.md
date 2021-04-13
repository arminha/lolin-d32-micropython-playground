# lolin-d32-micropython-playground

## Hardware

The [LOLIN D32](https://docs.wemos.cc/en/latest/d32/d32.html) is an ESP32 board with Wifi and Bluetooth.

## MicroPython

Tutorials

* [Getting started with MicroPython on the ESP32](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
* [ESP32 Tutorial using MicroPython](https://www.youtube.com/watch?v=QopRAwUP5ds)

Reference

* [General information about the ESP32 port](https://docs.micropython.org/en/latest/esp32/general.html)
* [Quick reference for the ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html)

## Serial Console with Python REPL

Use [minicom](https://wiki.emacinc.com/wiki/Getting_Started_With_Minicom)

```sh
minicom -D /dev/ttyUSB0 minirc.dfl
```

## Manage files in the board file system

Use [ampy](https://github.com/scientifichackers/ampy)

```sh
# list files
ampy ls

# read files
ampy get FILENAME

# write files
ampy put FILENAME
```

## Blinking LED

```python
from machine import Pin

# GPIO 5 is the build-in LED
p = Pin(5, Pin.OUT)
p.value(0) # LED on
p.value(1) # LED off
```

## Environment

Create a virtualenv with tools and dependencies

```sh
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
