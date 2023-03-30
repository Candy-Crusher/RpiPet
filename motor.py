import RPi.GPIO as GPIO
import time
 
#设置GPIO模式
GPIO.setmode(GPIO.BOARD)

class CarMove(object):
    def __init__(self):
        IN1 = 11
        IN2 = 12
        IN3 = 13
        IN4 = 15

        GPIO.setup(IN1, GPIO.OUT)  # GPIO input/output definiation
        GPIO.setup(IN2, GPIO.OUT)
        GPIO.setup(IN3, GPIO.OUT)
        GPIO.setup(IN4, GPIO.OUT)

        self.p1 = GPIO.PWM(IN1, 500)  # PWM initialization: 500 Hz
        self.p2 = GPIO.PWM(IN2, 500)
        self.p3 = GPIO.PWM(IN3, 500)
        self.p4 = GPIO.PWM(IN4, 500)

        self.p1.start(0)  # motors start
        self.p2.start(0)
        self.p3.start(0)
        self.p4.start(0)

    def pwmforward(self,speed):
        self.p1.ChangeDutyCycle(0)
        self.p2.ChangeDutyCycle(speed)
        self.p3.ChangeDutyCycle(speed)
        self.p4.ChangeDutyCycle(0)
        
    def pwmbackward(self,speed):
        self.p1.ChangeDutyCycle(speed)
        self.p2.ChangeDutyCycle(0)
        self.p3.ChangeDutyCycle(0)
        self.p4.ChangeDutyCycle(speed)
        
    def pwmleft(self,speed):
        self.p1.ChangeDutyCycle(0)
        self.p2.ChangeDutyCycle(0)
        self.p3.ChangeDutyCycle(speed)
        self.p4.ChangeDutyCycle(0)
        
    def pwmright(self,speed):
        self.p1.ChangeDutyCycle(0)
        self.p2.ChangeDutyCycle(speed)
        self.p3.ChangeDutyCycle(0)
        self.p4.ChangeDutyCycle(0)
    
    def pwmstop(self):
        self.p1.stop()
        self.p2.stop()
        self.p3.stop()
        self.p4.stop()

if __name__ == '__main__':
    try:
        car = CarMove()
        while(1):
            car.pwmforward(90)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        car.pwmstop()
        GPIO.cleanup()