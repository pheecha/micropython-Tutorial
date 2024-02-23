from network import WLAN,STA_IF
import utime as time

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
#ใส่ Token ที่ได้จากBlynk
blynk = BlynkLib.Blynk('Mxx_NtsOTCICx9zXq4WHUq3hEk55jtB9')

@blynk.on("V0") #เชื่อมต่อกับ Pin V0 ของ Blynk
def v0_write_handler(value): #อ่านค่าจาก Pin V0 ของ Blynk
    print('Sw value: {}'.format(value[0]))

while True:
    blynk.run()