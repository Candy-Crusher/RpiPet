# Infrared obstacle avoidance module

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class CarInfrared(object):
    def __init__(self):
        self.infrared_right = 36 # GPIO setting (BCM coding)
        self.infrared_left = 37

        GPIO.setup(self.infrared_right, GPIO.IN)
        GPIO.setup(self.infrared_left, GPIO.IN)

    def InfraredMeasure(self):
        left_measure = GPIO.input(self.infrared_left)  # if there is an obstacle, GPIO will become 0; else, GPIO_input = 1;
        right_measure = GPIO.input(self.infrared_right)

        return [left_measure, right_measure]


if __name__ == '__main__':
    try:
        car = CarInfrared()
        while True:
            [left, right] = car.InfraredMeasure()
            print(left, right)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()