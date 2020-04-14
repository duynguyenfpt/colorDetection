import cv2
import numpy as np
#instantiate videocapture object (0 is for the default webcam)
cap = cv2.VideoCapture(0)
def nothing(x):
    pass

# create trackbars for color change
cv2.namedWindow('image')
cv2.createTrackbar('H','image',0,360,nothing)
cv2.createTrackbar('S','image',0,100,nothing)
cv2.createTrackbar('V','image',0,100,nothing)

# image
img = np.zeros((50,50,3), np.uint8)

# while(True):
#     #read frame from video file
#     ret, frame = cap.read()
#     hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     cv2.imshow('image',frame)
#     low_blue = np.array([94, 80, 2])
#     high_blue = np.array([126, 255, 255])
#     blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
#     blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
#     #if esc key pressed or no more video input
#     cv2.imshow("Blue", blue)
#     # h = cv2.getTrackbarPos('H','image')
#     # s = cv2.getTrackbarPos('S','image')
#     # v = cv2.getTrackbarPos('V','image')
#     # img[:] = cv2.cvtColor([[h,s,v]],cv2.COLOR_HSV2BGR)
#     cv2.imshow("image",img)
#     if cv2.waitKey(1) & 0xFF == 27 or ret==False:
#         break

h = cv2.getTrackbarPos('H', 'image')
s = cv2.getTrackbarPos('S', 'image')
v = cv2.getTrackbarPos('V', 'image')
img[:] = cv2.cvtColor(np.array([h,s,v],np.uint8),cv2.COLOR_HSV2BGR)

# When everything done, release the capture

cv2.destroyAllWindows()
cap.release()