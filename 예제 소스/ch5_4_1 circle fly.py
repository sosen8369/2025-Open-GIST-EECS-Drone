from time import sleep
from CodingRider.drone import *
from CodingRider.protocol import *

drone = Drone()
drone.open('COM4')

try:
    sleep(2)
    print('이륙')
    drone.sendTakeOff()
    sleep(1)
    drone.sendControlWhile(0, 0, 0, 50, 150)
    sleep(3.2)
    print('돌기')
    drone.sendControlWhile(50, 0, 50, 2, 3200)
    sleep(1)
    drone.sendControl(0, 0, 0, 0)
except Exception as e:
    print(e)
    traceback.print_exc()
finally:
    sleep(2)
    drone.sendLanding()
    print('착륙')
