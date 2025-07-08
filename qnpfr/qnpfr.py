import copy 
from keras.models import load_model  
import cv2 
import numpy as np
from time import sleep
import keyboard
from CodingRider.drone import *
from CodingRider.protocol import *

drone = Drone()
drone.open('COM4')

# is_takeoff 변수로 이륙했는지 확인합니다.
is_takeoff = False

np.set_printoptions(suppress=True)
model = load_model('keras_model.h5', compile=False)
class_names = open('labels.txt', 'r', encoding='UTF-8').readlines()
capture = cv2.VideoCapture(0)

while capture.isOpened():    
    ret, frame = capture.read()
    if not ret: 
        continue
    frame = cv2.flip(frame, 1)   
    frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)      
    origin_frame = copy.deepcopy(frame) 
    frame = np.asarray(frame, dtype=np.float32).reshape(1, 224, 224, 3)
    frame = (frame / 127.5) - 1    
    prediction = model.predict(frame,verbose=0)    
    index = np.argmax(prediction)   
    class_name = class_names[index]
    confidence_score = prediction[0][index] 
    class_name = class_name[2:].strip() 
    confidence_score = round(confidence_score * 100, 2)
    text = f'{class_name} : {confidence_score}%'
    
    # <엔터> 키를 누르면 영상을 분석합니다. 
    if keyboard.is_pressed('enter'):
        # 0번 클래스(takeoff)로 분류했고 이륙하지 않았다면 이륙합니다.
        if (index == 0 and not is_takeoff):
            cv2.putText(origin_frame, text, (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0))
            cv2.imshow('Machine Learning', origin_frame)
            print('이륙')       
            sleep(2)
            drone.sendTakeOff()
            sleep(5)
            print('이륙 완료')           
            is_takeoff = True
        # 1번 클래스(landing)로 분류했고 이륙했다면 착륙합니다.
        if (index == 1 and is_takeoff):
            cv2.putText(origin_frame, text, (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0))
            cv2.imshow('Machine Learning', origin_frame)
            print('착륙')
            drone.sendControlWhile(0, 0, 0, 0, 500) # 제자리에서 0.5초 멈춥니다.
            drone.sendLanding()
            sleep(3)
            print('착륙 완료') 
            is_takeoff = False
    # 안전을 위해서 키보드로 착륙/정지하는 코드도 추가합니다.
    if keyboard.is_pressed('space'):
        print('착륙')
        drone.sendControlWhile(0, 0, 0, 0, 500) 
        drone.sendLanding()
        sleep(3)
        print('착륙 완료')
        is_takeoff = False
    if keyboard.is_pressed('q'):
        print('정지')
        drone.sendControlWhile(0, 0, 0, 0, 500)
        drone.sendStop()
        sleep(3)
        is_takeoff = False
    if cv2.waitKey(1) == 27: 
        break

capture.release()
cv2.destroyAllWindows()
