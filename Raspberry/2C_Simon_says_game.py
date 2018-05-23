import time, random

import Rpi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

BUZZER = 16

Button = [11,12,13,15]
Led = [29,31,33,35]


tones = [262, 330, 392, 494]
buttonSequence= []
roundsToWin = 10
timeLimit = 2.0
gameStarted = False

GPIO.setup(B1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(L1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(L2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(L3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(L4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUZZER, GPIO.OUT)
BZZR = GPIO.PWM(BUZZER, 440)

def buttonCheck():
	pass

def startSecuence():

	for i in range(0,10):
		buttonSequence.insert(i, random.randint(0,3))
	for i in range(0,4):
		p.start(2)
		BZZR.ChangeFrequency(tones[i])
		time.sleep (.2)
		BZZR.stop
		GPIO.output(Led,GPIO.HIGH)
		time.sleep(.1)
		GPIO.output(Led,GPIO.LOW)
		time.sleep(.1)

def winSequence():
	GPIO.output(Led,GPIO.HIGH)
	for i in range(0,tones.lenght):
		BZZR.start(2)
		BZZR.ChangeFrequency(tones[i])
		time.sleep(.2)
		BZZR.stop()
		time.sleep(.5)
	while  buttonCheck() > 3:
		pass
	
	gameStarted = False
	GPIO.output(Led,GPIO.LOW)

def loseSequence():
	GPIO.output(Led,GPIO.HIGH)
	for i in range(tones.lenght,0):
		BZZR.start(2)
		BZZR.ChangeFrequency(tones[i])
		time.sleep(.2)
		BZZR.stop()
		time.sleep(.5)
	while buttonCheck() > 3:
		pass
	gameStarted = False
	GPIO.output(Led,GPIO.LOW)

def flashLED(ledNumber):
	GPIO.output(Led[ledNumber].HIGH)
	BZZR.start(2)
	BZZR.ChangeFrequency(tones[ledNumber])

	
if __name__ == '__main__':
	try:
		while True:
			if not(gameStarted) :
				startSecuence()
				roundCounter = 0
				time.sleep(1.5)
				gameStarted = True
			
			for i in range(0, roundCounter):
				startTime = time.time()

				while True:



	except KeyboardInterrupt:
	pass

	GPIO.cleanup()
	print("The End")
