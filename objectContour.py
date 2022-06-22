import cv2
import numpy as np

def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]*percent/100)
    height=int(frame.shape[0]*percent/100)
    dim=(width, height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    image=rescale_frame(frame,percent=50)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edge=cv2.Canny(gray,50,300)
    _,biner=cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
    contours,hierarchy=cv2.findContours(edge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    jumlah=str(len(contours))
    print("jumlah objek : ",jumlah)
    result_contour=cv2.drawContours(image,contours,-1,(0,255,0),2)

    cv2.imshow("Grayscale",gray)
    cv2.imshow("Canny",edge)
    cv2.imshow("Biner",biner)
    cv2.imshow("Result Contour",result_contour)
    
    if cv2.waitKey(1)==ord('p'):
        break

camera.release()
cv2.destroyAllWindows()
