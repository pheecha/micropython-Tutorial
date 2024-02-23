from machine import Pin
from utime import sleep

print("Hello, ESP32!") #พิมพ์ Hello, ESP32!

led = Pin(12, Pin.OUT) #กำหนดขา Led ที่ขา5
while True:
   led.on() #เปิดไฟ
   sleep(0.5) #รอเวลา 0.5 วินาที
   led.off() #ปิดไฟ
   sleep(0.5)