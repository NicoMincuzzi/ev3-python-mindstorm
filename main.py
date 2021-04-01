from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from time import sleep
from threading import Thread

from obstacle_sensors import ObstacleSensors
from ev3_server_socket import ServerSocket


# Initialize the EV3 Brick.
ev3 = EV3Brick()

obstacle_sensor = InfraredSensor(Port.S4)
reflection_sensor = ColorSensor(Port.S1)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# The DriveBase is composed of two motors, with a wheel on each motor.
# The wheel_diameter and axle_track values are used to make the motors
# move at the correct speed when you give a motor command.
# The axle track is the distance between the points where the wheels
# touch the ground.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

obstacleSensors = ObstacleSensors(robot=robot, color_sensor=reflection_sensor)


# Play a sound to tell us when we are ready to start moving
ev3.speaker.beep()

# def playtone():
#     for j in range(0,20):             # Do twenty times.
#         ev3.speaker.beep()  #1000Hz for 0.2s
#         sleep(0.5)

# t = Thread(target=playtone)
# t.start()
server_socket = ServerSocket()
server_socket.run()

while True:
    # Begin driving forward at 200 millimeters per second.
    robot.drive(200, 0)
    
    while obstacle_sensor.distance() < 10:
        robot.stop()
        robot.turn(45)
        wait(10)

    obstacleSensors.hole()
