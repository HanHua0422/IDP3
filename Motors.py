# From Telerobotics group assignment
# Global Function
# Global Variable
# Classes
from time import ctime
import binascii
import RPi.GPIO as GPIO
import time
import threading
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class motor():
    def __init__(self):
        self.ENA = 13
        self.ENB = 20
        self.IN1 = 19  # Right side motor forward
        self.IN2 = 16  # Right side motor reverse
        self.IN3 = 21  # Left side motor reverse
        self.IN4 = 26  # Left side motor forward
        self.Speed = 50
        self.PWMRight = None
        self.PWMLeft = None

    def motor_init(self):
        # GPIO initialize
        GPIO.setup(self.ENA, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.ENB, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN4, GPIO.OUT, initial=GPIO.LOW)
        self.PWMRight = GPIO.PWM(self.ENA, 1000)
        self.PWMLeft = GPIO.PWM(self.ENB, 1000)
        self.PWMRight.start(50)
        self.PWMLeft.start(50)
        self.PWMRight.ChangeDutyCycle(self.Speed)
        self.PWMLeft.ChangeDutyCycle(self.Speed)
        print("current speed: ", self.Speed)

    def pwm_plus(self):
        self.Speed += 10
        self.PWMRight.ChangeDutyCycle(self.Speed)
        self.PWMLeft.ChangeDutyCycle(self.Speed)
        print("current speed: ", self.Speed)

    def pwm_minus(self):
        self.Speed -= 10
        self.PWMRight.ChangeDutyCycle(self.Speed)
        self.PWMLeft.ChangeDutyCycle(self.Speed)
        print("current speed: ", self.Speed)

    # Define a function to move
    def move_forward(self):
        print("Robot Car moves forward")
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, True)
        GPIO.output(self.IN2, False)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, True)

    # Define a function to move back
    def move_back(self):
        print("Robot Car moves backward")
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, True)
        GPIO.output(self.IN3, True)
        GPIO.output(self.IN4, False)

    # Define a function to stop
    def stop(self):
        print("Robot Car stops")
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, False)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, False)

    # Define a function to turn left
    def turn_left(self):
        print("Robot Car turns left")
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, True)
        GPIO.output(self.IN2, False)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, False)

    # Define a function to turn right
    def turn_right(self):
        print("Robot Car turns right")
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, False)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, True)

    # Define a function to turn clockwise
    def turn_clock(self):
        print("Robot Car turns clockwise")
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, True)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, True)

    # Define a function to turn counter_clockwise
    def turn_counterclock(self):
        print("Robot Car turns counter clockwise")
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, True)
        GPIO.output(self.IN2, False)
        GPIO.output(self.IN3, True)
        GPIO.output(self.IN4, False)



def main():
    robot_motor = motor()
    robot_motor.motor_init()
    pg.init()
    size = (width, height) = (200, 200)
    color = 255, 255, 255
    screen = pg.display.set_mode(size)
    pg.display.set_caption('Robot Operating UI')
    move_flag = False
    direction = 0

    while True:
        if move_flag:
            if direction == 1:
                robot_motor.move_forward()
            elif direction == 2:
                robot_motor.move_back()
            elif direction == 3:
                robot_motor.turn_()
            elif direction == 4:
                robot_motor.turn_right()
            else:
                pass

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            else:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        move_flag = True
                        direction = 1
                    elif event.key == pg.K_DOWN:
                        move_flag = True
                        direction = 2
                    elif event.key == pg.K_LEFT:
                        move_flag = True
                        direction = 3
                    elif event.key == pg.K_RIGHT:
                        move_flag = True
                        direction = 4

                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        move_flag = False
                        robot_motor.stop()
                    elif event.key == pg.K_DOWN:
                        move_flag = False
                        robot_motor.stop()
                    elif event.key == pg.K_LEFT:
                        move_flag = False
                        robot_motor.stop()
                    elif event.key == pg.K_RIGHT:
                        move_flag = False
                        robot_motor.stop()

def testpwm():
    robot_motor = motor()
    robot_motor.motor_init()
    robot_motor.move_forward()
    time.sleep(1)
    print(robot_motor.Speed)
    robot_motor.stop()
    time.sleep(1)

    robot_motor.PWMRight.start(0)
    robot_motor.PWMLeft.start(0)

    robot_motor.Speed += 20
    robot_motor.PWMRight.ChangeDutyCycle(robot_motor.Speed)
    robot_motor.PWMLeft.ChangeDutyCycle(robot_motor.Speed)
    robot_motor.move_forward()
    time.sleep(1)
    print(robot_motor.Speed)
    robot_motor.stop()
    time.sleep(1)

    robot_motor.Speed += 20
    robot_motor.PWMRight.ChangeDutyCycle(robot_motor.Speed)
    robot_motor.PWMLeft.ChangeDutyCycle(robot_motor.Speed)
    robot_motor.move_forward()
    time.sleep(1)
    print(robot_motor.Speed)
    robot_motor.stop()
    time.sleep(1)

    robot_motor.Speed += 10
    robot_motor.PWMRight.ChangeDutyCycle(robot_motor.Speed)
    robot_motor.PWMLeft.ChangeDutyCycle(robot_motor.Speed)
    robot_motor.move_forward()
    time.sleep(1)
    print(robot_motor.Speed)
    robot_motor.stop()
    time.sleep(1)

    robot_motor.PWMRight.stop()
    robot_motor.PWMLeft.stop()
    robot_motor.stop()


# Excute
if __name__ == "__main__":
    main()
