from machine import Pin
from utime import sleep
print("Hello, ESP32!") #พิมพ์ Hello, ESP32!

led = Pin(5, Pin.OUT) #กำหนดขา Led ที่ขา 5  
for i in range(5): #ทำซ้ำ 5 รอบ จาก 0-4
     print(i)
     led.value(1) #LED เปิด
     sleep(1) #รอเวลา 1 วินาที
     led.value(0) #LED ปิด
     sleep(1) #รอเวลา 1 วินาที
  