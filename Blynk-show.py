from network import WLAN,STA_IF
import utime as time
import machine
from machine import Pin 
# Network Setup
ssid = 'OooO' #ชื่อwifi
password = 'a1234567' #รหัสwifi
wlan = WLAN(STA_IF)
wlan.active(True)
print('Connecting...')
wlan.connect(ssid,password) #เชื่อมต่อ wifi
while not wlan.isconnected():
    pass
print(wlan.ifconfig()) #แสดงค่า ip ที่เชื่อมต่อสำเร็จ
    
import BlynkLib
from dht import DHT11
# Initialize Blynk
blynk = BlynkLib.Blynk('Mxx_NtsOTCICx9zXq4WHUq3hEk55jtB9')

dht = DHT11(Pin(13)) #กำหนดขาเซนเซอร์

while True:
  blynk.run()
  
  dht.measure() #วัดอุณภูมิ
  temperature = dht.temperature() #เก็บค่าอุณหภูมิไว้ใน temperature 
  print("Temperature:", temperature, "°C") #แสดงอุณภูมิ
  blynk.virtual_write(3,temperature) #ส่งข้อมูลไปแสดงที่Blynk
  
  time.sleep(0.5)
   