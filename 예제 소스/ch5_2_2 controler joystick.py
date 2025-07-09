from time import sleep
from CodingRider.drone import *
from CodingRider.protocol import *

def eventJoystick(joystick):
    print(joystick.left.x, joystick.left.y,
          joystick.right.x, joystick.right.y)

drone = Drone()
drone.open('COM4')
drone.setEventHandler(DataType.Joystick, eventJoystick)
drone.sendPing(DeviceType.Controller)

