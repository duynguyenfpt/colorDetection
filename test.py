import cv2
import numpy as np

img = cv2.imread("testcolor.png")
# cv2.imshow("a",img)
# cv2.waitKey(0)
# print(img[:,:,0])
# print(img[:,:,1])
# print(img[:,:,2])
# cv2.imshow("img",img)
# cv2.waitKey(0)
green = np.zeros((150,150,3), np.uint8)

green[:,:,0] = 62
green[:,:,1] = 176
green[:,:,2] = 210
# print(green[:,:,0])
# print(green[:,:,1])
# print(green[:,:,2])
green = cv2.cvtColor(green,cv2.COLOR_RGB2BGR)
print(cv2.cvtColor(np.uint8([[[62,176,210]]]),cv2.COLOR_RGB2HSV))
cv2.imshow("green",green)
cv2.waitKey(0)
