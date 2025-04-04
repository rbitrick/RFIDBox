from machine import Pin, PWM
from mfrc522 import MFRC522
import utime
 
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)

led = Pin(25, Pin.OUT)

servo_pin = machine.Pin(18)
servo = PWM(servo_pin)

max_duty = 7864
min_duty = 1802
half_duty = int(max_duty/2)

#Set PWM frequency
frequency = 50
servo.freq (frequency)

print("Bring TAG closer...")
print("")
 
 
while True:
    led.off()
    reader.init()
    #Servo at 0 degrees
    servo.duty_u16(min_duty)
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            
            if card == 691066899 or card == 344444403:
                print("Card ID: "+ str(card)+" PASS: Green Light Activated")
                led.on()
                #Servo at 180 degrees
                servo.duty_u16(max_duty)
                utime.sleep_ms(10000)
            else:
                print("Card ID: "+ str(card)+" NOT ACCEPTED")
            
            
utime.sleep_ms(500) 
