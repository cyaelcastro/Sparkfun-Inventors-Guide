import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
import time

try:
	initTime = time.time()
	lcd = CharLCD(cols=16, rows=2,pin_rw=None,pin_rs=37,pin_e=35,pins_data=[33,31,29,23],numbering_mode=GPIO.BOARD)
	lcd.clear()	
	lcd.cursor_pos = (0,0)
	lcd.write_string('Hello World')
	while True:
		lcd.cursor_pos = (1,0)
		lcd.write_string(str(round(time.time()-initTime)))
		time.sleep(.998)

except KeyboardInterrupt:
	pass
GPIO.cleanup()
