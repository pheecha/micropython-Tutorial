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

# Import Library
from linenotify import LineNotify
# Set Line Token 
line = LineNotify('vC5cVahBp0m4VUvfoF69cFazpPW4TGA1yakazhIANG0')
# Notify text message 
line.notify('Hello World!')
# Notify sticker with message
line.notifySticker(3,240,'Nice Sticker')
# Notify image from URL with message
line.notifyImageURL('https://static.wikia.nocookie.net/chainsaw-man/images/1/1b/Pochita.PNG','Pochita')
