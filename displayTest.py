import numpy as np
import cv2

# Load image
img = cv2.imread('testImage.jpg', 0)

#Display image
cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27 or k == 'e':
    cv2.destroyAllWindows()
elif k == 's':
    cv2.imwrite('testWrite.jpg', img)
    cv2.destroyAllWindows()
