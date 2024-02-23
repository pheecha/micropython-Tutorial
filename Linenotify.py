from network import WLAN,STA_IF

# Network Setup
ssid = 'ชื่อไวไฟ'
password = 'รหัสไวไฟ'
wlan = WLAN(STA_IF)
wlan.active(True)
print('Connecting...')
wlan.connect(ssid,password)
while not wlan.isconnected():
    pass
print(wlan.ifconfig())

# Import Library
from linenotify import LineNotify
# Set Line Token 
line = LineNotify('Token_Line')
# Notify text message 
line.notify('Hello World!')
# Notify sticker with message
line.notifySticker(3,240,'Nice Sticker')
# Notify image from URL with message
line.notifyImageURL('https://static.wikia.nocookie.net/chainsaw-man/images/1/1b/Pochita.PNG','Pochita')
