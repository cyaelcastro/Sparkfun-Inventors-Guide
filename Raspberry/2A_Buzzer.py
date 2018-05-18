import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
BUZZER = 16

GPIO.setup(BUZZER, GPIO.OUT)

for i in range(0,5):
	GPIO.output(BUZZER,True)
	print "BUZZER: ON"
	time.sleep(1)

	GPIO.output(BUZZER,False)
	print "BUZZER: OFF"
	time.sleep(1)
	
GPIO.cleanup()
