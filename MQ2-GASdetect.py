import machine
import time

mq2 = machine.ADC(34) # กำหนดขาที่อ่านค่าเซนเซอร์ MQ-2 ที่ขา 34

while True:
    
    mq2_value = mq2.read()  # อ่านค่า analog จากเซ็นเซอร์ MQ-2
    print("MQ-2 Analog Value:", mq2_value) # แสดงค่าที่ได้
    time.sleep(0.5)
    

