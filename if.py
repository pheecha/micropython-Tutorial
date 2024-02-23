from machine import Pin
from utime import sleep

print("Hello, ESP32!") #พิมพ์ Hello, ESP32!

led = Pin(12, Pin.OUT) #กำหนดขา Led ที่ขา5
if (led.value() == 0): #ถ้าสถานะ led = 0 (ปิดอยู่)
    print("turn on LED")
    led.value(1) #เปิด LED (0=ปิด 1=เปิด)
else: #เป็นเท็จ
    print("turn off LED")
    led.value(0) #ปิด LED (0=ปิด 1=เปิด)