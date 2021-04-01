from pybricks.ev3devices import ColorSensor
from pybricks.tools import wait
from pybricks.robotics import DriveBase

class ObstacleSensors:
    
    def __init__(self, robot: DriveBase, color_sensor: ColorSensor):
        self._color_sensor = color_sensor
        self._robot = robot

    def hole(self):
        if self._color_sensor.reflection() < 10:
            self._robot.stop()
            self._robot.straight(-300)
            wait(10)
            self._robot.turn(360)
