import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD

try:

	lcd = CharLCD(cols=16, rows=2,pin_rw=None,pin_rs=37,pin_e=35,pins_data=[33,31,29,23],numbering_mode=GPIO.BOARD)
	lcd.crlf()	
	lcd.cursor_pos = (0,0)
	lcd.write_string('Hello World')
	lcd.cursor_pos = (1, 1)
	lcd.write_string('This is line 2')

except KeyboardInterrupt:
	pass
GPIO.cleanup()
