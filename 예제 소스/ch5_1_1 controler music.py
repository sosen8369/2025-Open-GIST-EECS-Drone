from time import *
from CodingRider.drone import *
from CodingRider.protocol import *

drone = Drone()   
drone.open('COM4') 
drone.sendBuzzerScale(BuzzerScale.G4, 500)
sleep(0.5) 
drone.sendBuzzerScale(BuzzerScale.G4, 500)
sleep(0.5) 
drone.sendBuzzerScale(BuzzerScale.A4, 500)
sleep(0.5) 
drone.sendBuzzerScale(BuzzerScale.A4, 500)
sleep(0.5)  
drone.sendBuzzerScale(BuzzerScale.G4, 500)
sleep(0.5) 
drone.sendBuzzerScale(BuzzerScale.G4, 500)
sleep(0.5) 
drone.sendBuzzerScale(BuzzerScale.E4, 1000)
sleep(1)
