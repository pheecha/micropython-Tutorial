import machine
import time
from network import WLAN,STA_IF

# Network Setup
ssid = 'OooO'
password = 'a1234567'
wlan = WLAN(STA_IF)
wlan.active(True)
print('Connecting...')
wlan.connect(ssid,password)
while not wlan.isconnected():
    pass
print(wlan.ifconfig())

from linenotify import LineNotify
mq2 = machine.ADC(34) # กำหนดขาที่อ่านค่าเซนเซอร์ MQ-2 ที่ขา 34

# Set Line Token 
line = LineNotify('vC5cVahBp0m4VUvfoF69cFazpPW4TGA1yakazhIANG0')

while True:
    
    mq2_value = mq2.read()  # อ่านค่า analog จากเซ็นเซอร์ MQ-2
    print("MQ-2 Analog Value:", mq2_value) # แสดงค่าที่ได้
    if(mq2_value > 3900): #หากค่ามากกว่า 3900
        line.notify('ไฟไหม้') # ส่งข้อความไปที่ไลน์
    time.sleep(0.5)
    