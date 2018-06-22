import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
import time
import random

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

def showStartSequence(lcd):
	
	lcd.clear()
	lcd.cursor_pos = (0,0)
	lcd.write_string("Category:")
	lcd.cursor_pos = (1,0)
	lcd.write_string("Animals")
	time.sleep(2)
	
	lcd.clear()
	
	lcd.clear()
	lcd.write_string("Get ready!")
	time.sleep(1)
	
	lcd.clear()
	
	lcd.cursor_pos = (0,0)
	lcd.write_string("3")
	time.sleep(1)
	
	lcd.clear()
	
	lcd.cursor_pos = (0,0)
	lcd.write_string("2")
	time.sleep(1)
	
	lcd.clear()
	
	lcd.cursor_pos = (0,0)
	lcd.write_string("1")
	time.sleep(1)
	
	lcd.clear()
	
def generateRandomOrder(sequence):
	for i in range(0,24):
		currentNumber = 0
		match = True
		while match == True:
			match = False
			currentNumber = random.randint(0,arraySize-1)
		
			for j in range(0, i+1):
				if currentNumber == sequence[j]:
					match = True
			sequence[i] = currentNumber

			
def gameOver(lcd):
	lcd.clear()

	lcd.cursor_pos = (0,0)
	lcd.write_string("Game over")

	lcd.cursor_pos = (1,0)
	lcd.write_string("Score:")
	lcd.write_string(str(roundNumber))

	bzzr.start(2)
	bzzr.ChangeFrequency(130)
	time.sleep(.25)
	bzzr.stop()
	time.sleep(.275)

	bzzr.start(2)
	bzzr.ChangeFrequency(73)
	time.sleep(.25)
	bzzr.stop()
	time.sleep(.275)

	bzzr.start(2)
	bzzr.ChangeFrequency(65)
	time.sleep(.15)
	bzzr.stop()
	time.sleep(.175)

	bzzr.start(2)
	bzzr.ChangeFrequency(98)
	time.sleep(.5)
	bzzr.stop()
	time.sleep(.5)

	while True:
		pass
	
def winner(lcd):
	roundNumber
	lcd.clear()
	lcd.cursor_pos = (0,7)
	lcd.write_string("YOU")
	lcd.cursor_pos = (1,7)
	lcd.write_string("WIN")

	bzzr.start(2)
	bzzr.ChangeFrequency(1318)
	time.sleep(.15)
	bzzr.stop()
	time.sleep(.175)

	bzzr.start(2)
	bzzr.ChangeFrequency(1567)
	time.sleep(.15)
	bzzr.stop()
	time.sleep(.175)

	bzzr.start(2)
	bzzr.ChangeFrequency(2637)
	time.sleep(.15)
	bzzr.stop()
	time.sleep(.175)

	bzzr.start(2)
	bzzr.ChangeFrequency(2093)
	time.sleep(.15)
	bzzr.stop()
	time.sleep(.175)

	bzzr.start(2)
	bzzr.ChangeFrequency(2349)
	time.sleep(.15)
	bzzr.stop()
	time.sleep(.175)

	bzzr.start(2)
	bzzr.ChangeFrequency(3135)
	time.sleep(.5)
	bzzr.stop()
	time.sleep(.5)


	while True:
		pass



if __name__ == '__main__':

	try:
		lcd = CharLCD(cols=16, rows=2,pin_rw=None,pin_rs=37,pin_e=35,pins_data=[33,31,29,23],numbering_mode=GPIO.BOARD)
		generateRandomOrder(sequence)
		showStartSequence(lcd)
		for i in range(0,arraySize):
			roundNumber += 1
			print str(roundNumber)
			lcd.clear()
			lcd.cursor_pos = (0,0)
			lcd.write_string(str(roundNumber))
			lcd.write_string(": ")
			print i
			print sequence[i]
			print words[sequence[i]]
			lcd.write_string(words[sequence[i]])
			print ("----")
			

			startTime = time.time()

			while(GPIO.input(Button)):
				roundedTime = int(timeLimit - (time.time() - startTime))
				lcd.cursor_pos = (1,14)
				lcd.write_string("  ")
				lcd.cursor_pos = (1,14)
				lcd.write_string(str(roundedTime))
				time.sleep(.1)
				if (time.time() - startTime > timeLimit):
					gameOver(lcd)
				if GPIO.input(Button) == False:
					bzzr.start(2)
					bzzr.ChangeFrequency(272)
					time.sleep(1)
					bzzr.stop()
		winner(lcd)

		

	except KeyboardInterrupt:
		pass
	GPIO.cleanup()
