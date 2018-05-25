import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

BUZZER = 16
B1 = 11
B2 = 13
B3 = 15


GPIO.setup(B1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUZZER, GPIO.OUT)

BZZR = GPIO.PWM(BUZZER,440)



#note  frequency
c = 262 
d = 294
e = 330
f = 349
g = 392
a = 440
b = 494



try:
	while True:
		InB1 = GPIO.input(B1)
		InB2 = GPIO.input(B2)
		InB3 = GPIO.input(B3)	
		if InB1 == False:
			print ("B1")
			BZZR.start(2)
			BZZR.ChangeFrequency(a)
			time.sleep(0.2)
		elif InB2 == False:
		        print ("B2")
			BZZR.start(2)
	        	BZZR.ChangeFrequency(d)
			time.sleep(0.2)
		elif InB3 == False:
		        print ("B3")
			BZZR.start(2)
			BZZR.ChangeFrequency(f)
			time.sleep(0.2)
			BZZR.stop()
except KeyboardInterrupt:
	pass
print("The End")
GPIO.cleanup()
