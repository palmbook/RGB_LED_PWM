from OPi import GPIO
import time
import numpy as np

# Set board to Orange Pi Zero 2
GPIO.setboard(GPIO.H616)
GPIO.setmode(GPIO.BOARD)

RED_PIN = 23
GREEN_PIN = 21
BLUE_PIN = 19

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Set GPIO to PWM mode with frequency of 256Hz
# Frequency can be any number above 0
# I chose 256 because we are going to use 8-bit per channel
red = GPIO.PWM(RED_PIN, 256)
green = GPIO.PWM(GREEN_PIN, 256)
blue = GPIO.PWM(BLUE_PIN, 256)

red.start(0)
green.start(0)
blue.start(0)

for _ in range(10):
    # Random 3 integers
    target = np.random.randint(0, high=255, size=3)
    
    # Modulate duty cycle from 0-100
    # We convert from 8-bit (0-255) to 0-100
    red.ChangeDutyCycle(target[0] * 100 / 256)
    green.ChangeDutyCycle(target[1] * 100 / 256)
    blue.ChangeDutyCycle(target[2] * 100 / 256)
    time.sleep(5)

# stop PWM
red.stop()
green.stop()
blue.stop()

GPIO.cleanup()
