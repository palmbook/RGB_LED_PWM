from OPi import GPIO
import time
import numpy as np

GPIO.setboard(GPIO.H616)
GPIO.setmode(GPIO.BOARD)
RED_PIN = 23
GREEN_PIN = 21
BLUE_PIN = 19
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

red = GPIO.PWM(RED_PIN, 256)
green = GPIO.PWM(GREEN_PIN, 256)
blue = GPIO.PWM(BLUE_PIN, 256)

red.start(0)
green.start(0)
blue.start(0)

for _ in range(10):
    target = np.random.randint(0, high=255, size=3)
    red.ChangeDutyCycle(target[0] * 100 / 256)
    green.ChangeDutyCycle(target[1] * 100 / 256)
    blue.ChangeDutyCycle(target[2] * 100 / 256)
    time.sleep(5)

red.stop()
green.stop()
blue.stop()
GPIO.cleanup()
