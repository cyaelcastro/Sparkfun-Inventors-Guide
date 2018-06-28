import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

motor = 11
inA = 35
inB = 37

GPIO.setup(motor,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(inA,GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(inB,GPIO.OUT, initial = GPIO.LOW)
motorEnable = GPIO.PWM(motor,50)


speed = 0
motorEnable.start(0)
try:
	while speed < 100:
		print speed
		motorEnable.ChangeDutyCycle(speed)
		time.sleep(5)
		speed += 10


except KeyboardInterrupt:
	pass
GPIO.cleanup()