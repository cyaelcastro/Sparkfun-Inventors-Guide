import time, random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

BUZZER = 16
Button = [11,12,13,15]
Led = [29,31,33,35]
tones = [262, 330, 392, 494]

buttonSequence= [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
roundsToWin = 10
timeLimit = 4.0
global gameStarted
gameStarted = False
pressedButton = 4
#global roundCounter
#roundCounter = 1 
GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Led, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUZZER, GPIO.OUT)
BZZR = GPIO.PWM(BUZZER, 440)


def flashLED(ledNumber):
	GPIO.output(Led[ledNumber],GPIO.HIGH)
	BZZR.start(2)
	BZZR.ChangeFrequency(tones[ledNumber])

def allLEDoff():
	GPIO.output(Led,GPIO.LOW)
	BZZR.stop()

def buttonCheck():
	if GPIO.input(Button[0]) == False:
		
		return 0
	elif GPIO.input(Button[1]) == False:
		
		return 1
	elif GPIO.input(Button[2]) == False:
		
		return 2
	elif GPIO.input(Button[3]) == False:
		
		return 3
	else:
		#print ("B4 Default")
		return 4

def startSecuence():
	for i in range(0,roundsToWin):
		#buttonSequence[i] = random.randint(0,3)
		pass
	
	for i in range(0,4):
		BZZR.start(2)
		BZZR.ChangeFrequency(tones[i])
		time.sleep (0.2)
		BZZR.stop()
		GPIO.output(Led,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(Led,GPIO.LOW)
		time.sleep(0.1)
	print (buttonSequence)
def winSequence():
	GPIO.output(Led,GPIO.HIGH)
	
	BZZR.start(2)
	BZZR.ChangeFrequency(1318)
	time.sleep(0.150)
	BZZR.stop()
	time.sleep(0.175)
	BZZR.start(2)
	BZZR.ChangeFrequency(1567)
	time.sleep(0.150)
	BZZR.stop()
	time.sleep(0.175)
	BZZR.start(2)
	BZZR.ChangeFrequency(2637)
	time.sleep(0.150)
	BZZR.stop()
	time.sleep(0.175)
	BZZR.start(2)
	BZZR.ChangeFrequency(2093)
	time.sleep(0.150)
	BZZR.stop()
	time.sleep(0.175)
	BZZR.start(2)
	BZZR.ChangeFrequency(2349)
	time.sleep(0.150)
	BZZR.stop()
	time.sleep(0.175)
	BZZR.start(2)
	BZZR.ChangeFrequency(3135)
	time.sleep(0.150)
	BZZR.stop()
	time.sleep(0.175)

	pressedButton = buttonCheck()
	while  pressedButton > 3:
		pressedButton = buttonCheck()
		time.sleep(0.01)
	time.sleep(.1)
	global gameStarted
	gameStarted = False
	#GPIO.output(Led,GPIO.LOW)
	

def loseSequence():
	
	GPIO.output(Led,GPIO.HIGH)
	BZZR.start(2)
	BZZR.ChangeFrequency(130)
	time.sleep(0.25)
	BZZR.stop()
	time.sleep(0.275)
	BZZR.start(2)
	BZZR.ChangeFrequency(73)
	time.sleep(0.250)
	BZZR.stop()
	time.sleep(0.275)
	BZZR.start(2)
	BZZR.ChangeFrequency(65)
	time.sleep(0.150)
	BZZR.stop()
	time.sleep(0.175)
	BZZR.start(2)
	BZZR.ChangeFrequency(98)
	time.sleep(0.50)
	BZZR.stop()
	time.sleep(0.5)
	

	pressedButton = buttonCheck()
	while pressedButton > 3:
		pressedButton = buttonCheck()
		time.sleep(0.01)
	time.sleep(0.2)
	global gameStarted
	gameStarted = False
	
if __name__ == '__main__':
	try:
		while True:
			if gameStarted == False :
	
				startSecuence()
				global roundCounter 
				roundCounter = 1
	
				time.sleep(1.5)
	
				gameStarted = True
			for i in range(0,roundCounter): #F1
	
				flashLED(buttonSequence[i])
				time.sleep(0.2)
				allLEDoff()
				time.sleep(0.2)

			for i in range(0, roundCounter): #F2
				
				startTime = time.time()

				while True:
	
					pressedButton = buttonCheck()
	
					if pressedButton < 4:
						
						flashLED(pressedButton)
						
						if pressedButton == buttonSequence[i]:
							time.sleep(.250)
							allLEDoff()
							break
						else:
							loseSequence()
							break
					else:
						allLEDoff()
					if time.time() - startTime > timeLimit:
						loseSequence()
						break
					time.sleep(0.05)

			roundCounter = roundCounter + 1

			if roundCounter >= roundsToWin:
				winSequence()
			time.sleep(.5)
	except KeyboardInterrupt:
		pass
	GPIO.cleanup()
	print("The End")
