import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
import time

Button = 18
Buzzer = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Buzzer, GPIO.OUT)
bzzr = GPIO.PWM(Buzzer,440)

arraySize = 25
timeLimit = 15
startTime = 0
roundNumber = 0

words = ["moose", "beaver", "bear", "goose", "dog", "cat", "squirrel", "bird", "elephant", "horse", 
 "bull", "giraffe", "seal", "bat", "skunk", "turtle", "whale", "rhino", "lion", "monkey", 
 "frog", "alligator", "kangaroo", "hippo", "rabbit"]
sequence = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def showStartSequence():
	pass
def generateRandomOrder():
	pass
def gameOver
	pass
def winner
	pass

if __name__ == '__main__':

	try:
		lcd = CharLCD(cols=16, rows=2,pin_rw=None,pin_rs=37,pin_e=35,pins_data=[33,31,29,23],numbering_mode=GPIO.BOARD)
		for i in range(0,arraySize)
			lcd.crlf()
			lcd.cursor_pos = (0,0)
			lcd.write_string(str(roundNumber))
			lcd.write_string(": ")
			lcd.write_string(words[sequence[i]])
			startTime = time.time()

			while(GPIO.INPUT(Button)):
				roundedTime = round(timeLimit - (time.time() - startTime))
				led.cursor_pos = (1,14)
				led.write_string("  ")
				lcd.cursor_pos = (1,14)
				lcd.write_string(str(roundedTime))
				time.sleep(0.015) 
				if (time.time() - startTime > timeLimit):
					gameOver()
				if GPIO.INPUT(Button) == False:
					bzzr.start(2)
					bzzr.ChangeFrequency(272)
					bzzr.sleep(1)
					bzzr.stop()
		winner()

		

	except KeyboardInterrupt:
		pass
	GPIO.cleanup()
