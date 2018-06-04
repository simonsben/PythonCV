import cv2
import numpy as np

img = cv2.imread('testImage3.jpg')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(grey, 100, 150, apertureSize = 3)

minLineLength = 75
maxLineGap = 20

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)

print(lines)

for line in lines:
    for (x1, y1, x2, y2) in line:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Hough test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
