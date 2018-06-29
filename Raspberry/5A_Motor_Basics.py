import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

motor = 11
inA = 35
inB = 37

GPIO.setup(motor,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(inA,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(inB,GPIO.OUT, initial = GPIO.LOW)
motorEnable = GPIO.PWM(motor,50)


speed = 0
motorEnable.start(0)
try:
	while True:
		speed = int(raw_input("Please enter the motor speed you want ( -100 - 100): "))
		if speed >= -100 and speed <= 100:
			if speed >= 0:
				GPIO.output(inA, GPIO.LOW)
				GPIO.output(inB, GPIO.HIGH)
				motorEnable.ChangeDutyCycle(speed)
			else:
				GPIO.output(inA, GPIO.HIGH)
				GPIO.output(inB, GPIO.LOW)
				motorEnable.ChangeDutyCycle(abs(speed))

		else:
			print ("Try again")
				


except KeyboardInterrupt:
	pass

except ValueError:
	print ("That speed isn't possible :(")
GPIO.cleanup()