import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
TRIG = 40
ECHO = 38
#	   R  G  B
LED = [33,31,29]
BUZZER = 16
SERVO = 11

GPIO.setup(LED,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(SERVO, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

pwmServo = GPIO.PWM(SERVO,50)
pwmServo.start(0)

def SetAngle(angle):
	duty = angle / 18 +2
	GPIO.output(SERVO, GPIO.HIGH)
	pwmServo.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(SERVO, GPIO.LOW)
	pwmServo.ChangeDutyCycle(0)

def getDistance():
	GPIO.output(TRIG,GPIO.HIGH)
	#time.sleep(0.00001)
	time.sleep(0.001)
	GPIO.output(TRIG,GPIO.LOW)
	while GPIO.input(ECHO) == 0:
		pulseStart = time.time()
	while GPIO.input(ECHO) ==1:
		pulseEnd = time.time()
	pulseDuration = pulseEnd - pulseStart
	distance = round(pulseDuration * 17150,2)
	return distance
if __name__ == '__main__':

	try:
		print ("Start")
		while True:
			distance = getDistance()
			if distance < 10:
				#RED LIGHT
				#print ("RED LIGHT")
				GPIO.output(LED[0],GPIO.HIGH)
				GPIO.output(LED[1],GPIO.LOW)
				GPIO.output(LED[2],GPIO.LOW)
				GPIO.output(BUZZER,GPIO.HIGH)
				SetAngle(45)
				time.sleep(.1)
				GPIO.output(BUZZER,GPIO.LOW)
				SetAngle(135)
			elif distance > 10 and distance < 20:
				#YELLOW LIGHT
				#print ("YELLOW LIGHT")
				GPIO.output(LED[0],GPIO.HIGH)
				GPIO.output(LED[1],GPIO.HIGH)			
				GPIO.output(LED[2],GPIO.LOW)
			else:
				#GREEN LIGHT
				#print ("GREEN LIGHT")
				GPIO.output(LED[0],GPIO.LOW)
				GPIO.output(LED[1],GPIO.HIGH)
				GPIO.output(LED[2],GPIO.LOW)

			#print "Distancia: "+str(distance)+" cm"
			time.sleep(.1)
	except KeyboardInterrupt:
		pass
	print("The End")
	GPIO.cleanup()
