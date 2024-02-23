from machine import Pin
import utime

# กำหนดขา GPIO ที่เชื่อมต่อกับ Buzzer module
buzzer_pin = Pin(25, Pin.OUT)

def beep(duration_ms):
    # ส่งสัญญาณ low เพื่อเปิด Buzzer
    buzzer_pin.value(0)
    
    # รอเป็นเวลา duration_ms
    utime.sleep_ms(duration_ms)
    
    # ส่งสัญญาณ high เพื่อปิด Buzzer
    buzzer_pin.value(1)

# เรียกใช้ฟังก์ชัน beep โดยกำหนดเวลาที่ Buzzer ต้องทำงาน (เปิด-ปิด)
beep(500)  # ตัวอย่าง: Buzzer เปิด-ปิด เป็นเวลา 500 มิลลิวินาที

