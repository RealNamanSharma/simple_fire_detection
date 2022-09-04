import asyncio
import cv2 
from playsound import playsound

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)
    
    for x,y,w,h in fire:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,199), 2)
        print('fire detected!!!')
        playsound('sound.mp3')    
        asyncio.sleep(2)
        

    cv2.imshow("NAAMAN COPYRIGHT HEHE", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('f'):
        break


#by naman3428
#use f key to close cv2 window
#before running this please open command prompt and type "pip install opencv-python"
# ravi
