import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

motorLeft = 11
motorRight = 12

inA = 31
inB = 33
inC = 35
inD = 37


GPIO.setup(motorLeft,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(motorRight,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(inA,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(inB,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(inC,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(inD,GPIO.OUT, initial = GPIO.LOW)
motorLeftEnable = GPIO.PWM(motorLeft,50)
motorRightEnable = GPIO.PWM(motorRight,50)


motorLeftEnable.start(0)
motorRightEnable.start(0)

driveTime = 1
turnTime = 2

def leftMotor(motorSpeed):
	if motorSpeed > 0:
		GPIO.output(inA, GPIO.LOW)
		GPIO.output(inB, GPIO.HIGH)
	elif motorSpeed < 0:
		GPIO.output(inA, GPIO.HIGH)
		GPIO.output(inB, GPIO.LOW)
	elif motorSpeed == 0:
		GPIO.output(inA, GPIO.LOW)
		GPIO.output(inB, GPIO.LOW)
	motorLeftEnable.ChangeDutyCycle(abs(motorSpeed))


def rightMotor(motorSpeed):
	if motorSpeed > 0:
		GPIO.output(inC, GPIO.LOW)
		GPIO.output(inD, GPIO.HIGH)
	elif motorSpeed < 0:
		GPIO.output(inC, GPIO.HIGH)
		GPIO.output(inD, GPIO.LOW)
	elif motorSpeed == 0:
		GPIO.output(inC, GPIO.LOW)
		GPIO.output(inD, GPIO.LOW)
	motorRightEnable.ChangeDutyCycle(abs(motorSpeed))

try:
	while True:
		print ("Please enter the direction and speed")
		print("f = forward, b = backward, r = turn right, l = turn left");
		speedAndDir = raw_input("Example comand f 50: ")
		direction = speedAndDir[0]
		speed = speedAndDir[2:]
		speed = int(speed)

		if (direction == "f" or direction == "b" or direction == "l" or direction == "r") and (speed >= -100 or speed <= 100):

			if direction == "f":
				leftMotor(80)
				rightMotor(80)
				time.sleep(driveTime * speed )
				leftMotor(0)
				rightMotor(0)
			elif direction == "b":
				leftMotor(-80)
				rightMotor(-80)
				time.sleep(driveTime * speed )
				leftMotor(0)
				rightMotor(0)
			elif direction == "l":
				leftMotor(-80)
				rightMotor(100)
				time.sleep(turnTime * speed )
				leftMotor(0)
				rightMotor(0)
			elif direction == "r":
				leftMotor(100)
				rightMotor(-80)
				time.sleep(turnTime * speed )
				leftMotor(0)
				rightMotor(0)

		else:
			print ("Try again")
		
except KeyboardInterrupt:
	pass

except ValueError:
	print ("That speed and direction aren't possible :(")
GPIO.cleanup()