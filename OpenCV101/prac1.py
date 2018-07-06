import cv2
import numpy as np

image = cv2.imread('input.jpg')
cv2.imshow('Output', image)
cv2.waitKey()

b, g, r = cv2.split(image)

cv2.imshow('Output', b)
cv2.waitKey()

cv2.imshow('Output', g)
cv2.waitKey()

cv2.imshow('Output', r)
cv2.waitKey()
cv2.destroyAllWindows()

print(image[10,50])
print(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)[10,50])

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('hsv h', hsv[:,:,0])
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('hsv s', hsv[:,:,1])
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('hsv v', hsv[:,:,2])
cv2.waitKey()
cv2.destroyAllWindows()

print('B Shape', b.shape)