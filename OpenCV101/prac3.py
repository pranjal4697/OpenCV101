import cv2
import numpy as np

base_image = np.zeros((512,512,3), np.uint8)
cv2.imshow('Base Image', base_image)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.line(base_image, (0,0), (511,511), (255,123,99), 3)
cv2.imshow('Line on Base', base_image)
cv2.waitKey()
cv2.destroyAllWindows()

base_image = np.zeros((512,512,3), np.uint8)
cv2.rectangle(base_image, (20,20), (111,111), (255,123,99), 3)
cv2.imshow('Reaactangle on Base', base_image)
cv2.waitKey()
cv2.destroyAllWindows()

base_image = np.zeros((512,512,3), np.uint8)
cv2.circle(base_image, (220,220), 100, (255,123,99), -1)
cv2.imshow('Circle on Base', base_image)
cv2.waitKey()
cv2.destroyAllWindows()

base_image = np.zeros((512,512,3), np.uint8)
cv2.putText(base_image, 'Hello!', (220,220), cv2.FONT_HERSHEY_COMPLEX, 2, (255,123,99), 3)
cv2.imshow('Text on Base', base_image)
cv2.waitKey()
cv2.destroyAllWindows()