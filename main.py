from machine import Pin
from mfrc522 import MFRC522
import utime
 
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)

led = Pin(25, Pin.OUT)

print("Bring TAG closer...")
print("")
 
 
while True:
    led.off()
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            
            if card == 691066899 or card == 344444403:
                print("Card ID: "+ str(card)+" PASS: Green Light Activated")
                led.on()
                utime.sleep_ms(2000)
            else:
                print("Card ID: "+ str(card)+" NOT ACCEPTED")
            
            
utime.sleep_ms(500) 
