import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
servo = 11
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo,50) #PIN at 50Hz
pwm.start(0) #0 duty cycle

def SetAngle(angle):
	duty = angle / 18 +2
	GPIO.output(servo, GPIO.HIGH)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(servo, GPIO.LOW)
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
