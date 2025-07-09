from time import sleep
import keyboard
from CodingRider.drone import *
from CodingRider.protocol import *

drone = Drone()
drone.open('COM4')
speed = 50

while True:
    if keyboard.is_pressed('enter'):   
        print('이륙')       
        sleep(2)
        drone.sendTakeOff()
        sleep(5)
        print('이륙 완료') 
    if keyboard.is_pressed('space'):
        print('착륙')
        drone.sendControlWhile(0, 0, 0, 0, 500) 
        drone.sendLanding()
        sleep(3)
        print('착륙 완료')
    if keyboard.is_pressed('q'):
        print('정지')
        drone.sendControlWhile(0, 0, 0, 0, 500)
        drone.sendStop()
        sleep(3)   
    if keyboard.is_pressed('esc'):
        print('프로그램 종료')
        break 
    if keyboard.is_pressed('up'):
        while keyboard.is_pressed('up'):
            drone.sendControl(0, speed, 0, 0)
        drone.sendControl(0, 0, 0, 0) 
    if keyboard.is_pressed('down'):
        while keyboard.is_pressed('down'):
            drone.sendControl(0, -speed, 0, 0)
        drone.sendControl(0, 0, 0, 0)  
    if keyboard.is_pressed('left'):
        while keyboard.is_pressed('left'):
            drone.sendControl(-speed, 0, 0, 0)
        drone.sendControl(0, 0, 0, 0) 
    if keyboard.is_pressed('right'):
        while keyboard.is_pressed('right'):
            drone.sendControl(speed, 0, 0, 0)
        drone.sendControl(0, 0, 0, 0)
    if keyboard.is_pressed('w'):
        while keyboard.is_pressed('w'):
            drone.sendControl(0, 0, 0, speed)
        drone.sendControl(0, 0, 0, 0) 
    if keyboard.is_pressed('s'):
        while keyboard.is_pressed('s'):
            drone.sendControl(0, 0, 0, -speed)
        drone.sendControl(0, 0, 0, 0)
    if keyboard.is_pressed('a'):
        while keyboard.is_pressed('a'):
            drone.sendControl(0, 0, speed, 0)
        drone.sendControl(0, 0, 0, 0)
    if keyboard.is_pressed('d'):
        while keyboard.is_pressed('d'):
            drone.sendControl(0, 0, -speed, 0)
        drone.sendControl(0, 0, 0, 0)  
    sleep(0.01)
