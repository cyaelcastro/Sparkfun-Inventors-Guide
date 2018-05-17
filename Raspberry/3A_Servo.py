import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
pwm = GPIO.PWM(03,50) #PIN 3 at 50Hz
pwm.start(0) #0 duty cycle

def SetAngle(angle):
	duty = angle / 18 +2
	GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)

if __name__ == "__main__":

	SetAngle(90)
	sleep(1)
	SetAngle(0)
	sleep(1)
	SetAngle(180)
	sleep(1)
	pwm.stop()
	GPIO.cleanup()
