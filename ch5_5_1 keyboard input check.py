from time import *
import keyboard

while True:
    print(keyboard.read_key())
    sleep(0.01)
    if keyboard.read_key() == 'esc':
        print('프로그램 종료')
        break

keyboard.is_pressed('키이름')
from time import *
import keyboard

while True:
    if keyboard.is_pressed('esc'):
        print('프로그램 종료')        
        break
    sleep(0.01)
