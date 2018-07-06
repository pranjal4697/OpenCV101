#PERSPECTIVE AND NON AFFINE TRANSFORMATION
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('scan.jpg')
cv2.imshow('original', image)
cv2.waitKey()

points_original = np.float32([[320,15],[700,215],[85,610],[538,780]])
points_result = np.float32([[0,0],[420,0],[0,594],[420,594]])
M = cv2.getPerspectiveTransform(points_original, points_result)
warped = cv2.warpPerspective(image, M, (420,594))

cv2.imshow('warpPerspective', warped)
cv2.waitKey()
cv2.destroyAllWindows()