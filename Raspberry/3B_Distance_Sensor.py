import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
TRIG = 40
ECHO = 38

GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO, GPIO.IN)

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
print "Distancia: "+str(distance)+" cm"
GPIO.cleanup()
