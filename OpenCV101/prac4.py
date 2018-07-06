import cv2
import numpy as np

#TRANSLATION
image = cv2.imread('input.jpg')
height, width = image.shape[:2]

quarter_height, quarter_width = -height/4, -width/4

T = np.float32([[1,0,quarter_height],[0,1,quarter_width]])

translated_image = cv2.warpAffine(image, T, (width, height))
cv2.imshow('translated_image', translated_image)
cv2.waitKey()
cv2.destroyAllWindows()

print (T)

#ROTATION	
M = cv2.getRotationMatrix2D((width/2, height/2), -30, .5)
rotated_image = cv2.warpAffine(image, M, (width,height))
cv2.imshow('rotated_image', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()
transposed_image = cv2.transpose(image)
cv2.imshow('transposed_image', transposed_image)
cv2.waitKey()
cv2.destroyAllWindows()
transposed_image1 = cv2.transpose(transposed_image)
cv2.imshow('transposed1_image', transposed_image1)
cv2.waitKey()
cv2.destroyAllWindows()
print (M)


#RESIZING OR SCALING
image_scaled = cv2.resize(image, None, fx=0.75, fy=0.75)
cv2.imshow('scaled_image', image_scaled)
cv2.waitKey()
cv2.destroyAllWindows()
image_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('scaled_image', image_scaled)
cv2.waitKey()
cv2.destroyAllWindows()
image_scaled = cv2.resize(image, (900,450), fx=0.75, fy=0.75,interpolation=cv2.INTER_AREA)
cv2.imshow('scaled_image', image_scaled)
cv2.waitKey()
cv2.destroyAllWindows()

#IMAGE PYRAMIDING
smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(image)
cv2.imshow('Pyramid Down', smaller)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('Pyramid Up', larger)
cv2.waitKey()
cv2.destroyAllWindows()

#CROPPING
height, width = image.shape[:2]
start_row, start_col = int(height*.25), int(width*.25)
end_row, end_col = int(height*.75), int(width*.65)
cropped_image = image[start_row:end_row, start_col:end_col]
cv2.imshow('cropped_image', cropped_image)
cv2.waitKey()
cv2.destroyAllWindows()

#ARITHMETIC OPERATIONS TO INCREASE/DECREASE INTENSITY
N = np.ones(image.shape, dtype = 'uint8') * 75
added = cv2.add(image, N)
cv2.imshow('added', added)
sub = cv2.subtract(image, N)
cv2.imshow('sub', sub)
cv2.waitKey()
cv2.destroyAllWindows()

#CONVOLUTION AND BLURRING
image = cv2.imread('elephant.jpg')
cv2.imshow('image', image)
cv2.waitKey()
kernel_3x3 = np.ones((3,3), np.float32) / 9
print(kernel_3x3)
blurred = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow('blurred', blurred)
cv2.waitKey()
kernel_7x7 = np.ones((7,7), np.float32) / 49
blurred = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow('blurred', blurred)
cv2.waitKey()
blur1 = cv2.blur(image, (3,3))
cv2.imshow('blur1', blur1)
cv2.waitKey()
blur2 = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow('blur2', blur2)
cv2.waitKey()
blur3 = cv2.medianBlur(image, 5)
cv2.imshow('blur3', blur3)
cv2.waitKey()
blur4 = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('blur4', blur4)
cv2.waitKey()
cv2.destroyAllWindows()
#DENOISING
cv2.imshow('image', image)
cv2.waitKey()
dns = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)
cv2.imshow('dns', dns)
cv2.waitKey()
cv2.destroyAllWindows()

#SHARPENING
cv2.imshow('image', image)
cv2.waitKey()
kernel_sharpening = np.array([[-1,-1,-1],
							  [-1,9,-1],
							  [-1,-1,-1]])
sharp = cv2.filter2D(image, -1, kernel_sharpening)
cv2.imshow('sharp', sharp)
cv2.waitKey()
cv2.destroyAllWindows()

#THRESHOLDING
# Load our image as greyscale 
image = cv2.imread('gradient.jpg',0)
cv2.imshow('Original', image)

# Values below 127 goes to 0 (black, everything above goes to 255 (white)
ret,thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('1 Threshold Binary', thresh1)

# Values below 127 go to 255 and values above 127 go to 0 (reverse of above)
ret,thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('2 Threshold Binary Inverse', thresh2)

# Values above 127 are truncated (held) at 127 (the 255 argument is unused)
ret,thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('3 THRESH TRUNC', thresh3)

# Values below 127 go to 0, above 127 are unchanged  
ret,thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('4 THRESH TOZERO', thresh4)

# Resever of above, below 127 is unchanged, above 127 goes to 0
ret,thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('5 THRESH TOZERO INV', thresh5)
cv2.waitKey(0) 
    
cv2.destroyAllWindows()

#DILATION AND EROSION
image = cv2.imread('opencv_inv.png', 0)
cv2.imshow('image', image)
cv2.waitKey()
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(image, kernel, iterations = 1)
cv2.imshow('erosion', erosion)
cv2.waitKey()
dilation = cv2.dilate(image, kernel, iterations =1)
cv2.imshow('dilation', dilation)
cv2.waitKey()
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)
cv2.waitKey()
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing', closing)
cv2.waitKey()
cv2.destroyAllWindows()  



