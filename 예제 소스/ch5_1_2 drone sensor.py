from time import sleep
from CodingRider.drone import *
from CodingRider.protocol import *

def eventMotion(motion):
    print(motion.anglePitch, motion.angleRoll)

drone = Drone()
drone.open('COM4')
drone.setEventHandler(DataType.Motion, eventMotion)

while True: 
    drone.sendRequest(DeviceType.Drone, DataType.Motion)
    sleep(0.1)
