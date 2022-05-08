from gpiozero import Robot, LineSensor, DistanceSensor
from signal import pause
from time import sleep

# GPIO pins
# Assign pins to left and right motors
robot = Robot(left=(7, 8), right=(9, 10))

# Assign pins to infrared sensors and ultrasonic sensor
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)
# robot should move backwards if obstacle gets within 10cm
ultra = DistanceSensor(23, 24, max_distance=1, threshold_distance=0.1)

# Constant loop
while True:
  left_detect = int(left_sensor.value)
  right_detect = int(right_sensor.value)
  ultra_detect = ultra.value
  ultra_sensor = format(round(ultra_detect,1)))
  
# Possible scenarios
# 1: left detects, right doesn't detect
  if left_detect == 1 and right_detect == 0:
    robot.turn_left()

# 2: right detects, left doesn't detect
  elif left_detect == 0 and right_detect == 1:
    robot.turn_right()

# 3: left and right detect
  elif left_detect == 1 and right_detect == 1:
    robot.move_forward()
  
# 4: left and right don't detect
  elif left_detect == 0 and right_detect == 0:
    robot.stop()
  
  elif ultra_sensor <= 0.1:
    robot.move_backwards()
