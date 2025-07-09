import cv2
import mediapipe as mp

capture = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
    ) as hands:

    while capture.isOpened():
        ret, frame = capture.read()
        if not ret:
            continue 
        frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        results = hands.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:            
            for hand_landmarks in results.multi_hand_landmarks: 
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS) 
                
                # 검지 손가락을 선택합니다.
                finger = hand_landmarks.landmark[8] 

                # 검지 손가락의 좌표로 텍스트를 만듭니다.
                # finger.x는 x좌표, finger.y는 y좌표입니다.
                # 소수점 둘째 자리까지 나타냅니다.
                text = 'x : {:.2f}, y : {:.2f}'.format(finger.x, finger.y)
                cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 1)                
        cv2.imshow('MediaPipe Hand Detection', frame)
        if cv2.waitKey(1) == 27:
            break
        
capture.release()
cv2.destroyAllWindows()
