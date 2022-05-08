from gpiozero import Robot, LineSensor
from signal import pause
from time import sleep

# GPIO pins
# Assign pins to left and right motors
robot = Robot(left=(7, 8), right=(9, 10))

# Assign pins to infrared sensors
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)

# Constant loop
while True:
  left_detect = int(left_sensor.value)
  right_detect = int(right_sensor.value)
  
# Possible scenarios
# 1: left detects, right doesn't detect
  if left_sensor.when_line and right_sensor.when_no_line:
    robot.turn_left()

# 2: right detects, left doesn't detect
  elif left_sensor.when_no_line and right_sensor.when_line:
    robot.turn_right()

# 3: left and right detect
  elif left_sensor.when_line and right_sensor.when_line:
    robot.move_forward()
  
# 4: left and right don't detect
  elif left_sensor.when_no_line and left_sensor.when_no_line:
    robot.stop()
