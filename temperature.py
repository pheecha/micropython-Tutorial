from machine import Pin  
from dht import DHT11
from time import sleep
dht = DHT11(Pin(13)) #กำหนดขาเซนเซอร์
while True:
  dht.measure() #วัดอุณภูมิและความชื้น
  
  temperature = dht.temperature() #เก็บค่าอุณหภูมิไว้ใน temperature 
  humidity = dht.humidity() #เก็บค่าความชื้นไว้ใน humidity
  
  print("Temperature:", temperature, "°C") #แสดงอุณภูมิ
  print("Humidity:", humidity, "%") #แสดงความชื้น
  
  sleep(0.5)
