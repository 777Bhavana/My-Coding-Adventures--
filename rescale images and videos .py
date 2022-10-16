from turtle import width
import cv2
import matplotlib.pyplot as plt

# the method if you ever need it !!

#  def rescaleFrame(frame,scale=0.75):
#       width= int(frame.shape[1] *scale)
#       height= int(frame.shape[0] *scale)
#       dimensions =(width,height)
#       return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)




# for images 
img =cv2.imread('bird.jpg')

def rescaleFrame(frame,scale=0.75):
    width= int(frame.shape[1] *scale)
    height= int(frame.shape[0] *scale)
    dimensions =(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

resized_img=rescaleFrame(img,scale=1.5)
cv2.imshow('the smaller image',resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()



# for videos 
def rescaleFrame(frame,scale=0.75):
    width= int(frame.shape[1] *scale)
    height= int(frame.shape[0] *scale)
    dimensions =(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

capture = cv2.VideoCapture('kunju.mp4') # cv2.VideoCapture(0) to capture from laptop's webcam 
while True:
    isTrue ,frame = capture.read()
    resized_vidFrame =rescaleFrame(frame=frame,scale=0.75)
    cv2.imshow('Video',resized_vidFrame)     
    if cv2.waitKey(0)and 0xFF==ord('d'):
        break


capture.release()
cv2.destroyAllWindows()

