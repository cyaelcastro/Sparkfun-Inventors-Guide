import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
TRIG = 40
ECHO = 38
#	   R  G  B
LED = [33,31,29]

GPIO.setup(LED,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO, GPIO.IN)


try:
	while True:
		GPIO.output(TRIG,GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(TRIG,GPIO.LOW)
		while GPIO.input(ECHO) ==0:
			pulseStart = time.time()
		while GPIO.input(ECHO) ==1:
			pulseEnd = time.time()
		pulseDuration = pulseEnd - pulseStart
		distance = pulseDuration * 17150
		distance = round(distance, 2)

		if distance < 10:
			#RED LIGHT
			GPIO.output(LED[0],GPIO.HIGH)
		elif distance > 10 and distance < 20:
			#YELLOW LIGHT
			GPIO.output(LED[0],GPIO.HIGH)
			GPIO.output(LED[1],GPIO.HIGH)			
		else:
			#GREEN LIGHT
			GPIO.output(LED[1],GPIO.HIGH)


		print "Distancia: "+str(distance)+" cm"
		time.sleep(2)
		GPIO.output(LED,GPIO.LOW)
except KeyboardInterrupt:
	pass
print("The End")
GPIO.cleanup()
