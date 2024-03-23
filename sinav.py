from machine import Pin, SoftI2C
import ssd1306
from time import sleep
from hcsr04 import HCSR04
# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
def ac(*args):
    for arg in args:
        arg.on()
def kapat(*args):
    for arg in args:
        arg.off()
        
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
pin4=Pin(4,Pin.OUT)
pin14=Pin(14,Pin.OUT)
while True:
    oled.fill(0)
    distance = sensor.distance_cm()
    if 1<= distance <=16:
        kapat(pin14)
        ac(pin4)
    elif 16<= distance <=24:
        kapat(pin4)
        ac(pin14)
    elif 20<=distance or distance >16:
        kapat(pin14)
        kapat(pin4)
    else:
        kapat(pin4)
        
    oled.text(str(distance),0,0)
    oled.show()
    sleep(0.5)
