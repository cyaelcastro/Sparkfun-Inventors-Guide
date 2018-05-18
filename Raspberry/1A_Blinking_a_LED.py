import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
LED = 16

GPIO.setup(LED, GPIO.OUT)

for i in range(0,5):
	GPIO.output(LED,True)
	print "LED: ON"
	time.sleep(2)

	GPIO.output(LED,False)
	print "LED: OFF"
	time.sleep(2)
	
GPIO.cleanup()
