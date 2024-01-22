import keyboard  # using module keyboard
import time
import cv2
import os


mainruncmmd ="python plate_recognition.py --api-key 3753074b221c6efa35368f1695763aef904b778c "

timestr=time.strftime("%Y%m%d-%H%M%S")
dir_path = 'Images/'
file_name= timestr +'.jpg'

path = dir_path +file_name

withfilepath = mainruncmmd + path 

cap = cv2.VideoCapture(0) 
cap.set(480, 640) 

cap.read()

while True:  
    try:  
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        if keyboard.is_pressed('s') or keyboard.is_pressed('S'):  # if key 'q' is pressed 
            print('IMAGE CAPTURED.......')
            print("ANALYZING IMAGE....")
            cv2.imwrite(path, frame)
            os.system(withfilepath)
            time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

           
    except:
        cap.release()
        #cv2.destroyAllWindows()
        break 



cap.release()
#cv2.destroyAllWindows()