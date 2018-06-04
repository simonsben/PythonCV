import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

img = cv2.imread('testImage2.jpg', 0)
edges = cv2.Canny(img, 100, 200)
edges2 = cv2.Canny(img, 170, 200)

cv2.namedWindow('EdgeTest')
cv2.createTrackbar('Min', 'EdgeTest', 0, 300, nothing)
cv2.createTrackbar('Max', 'EdgeTest', 0, 700, nothing)

# plt.subplot(211), plt.imshow(edges, cmap='gray')
# plt.title('Baseline edge'), plt.xticks([]), plt.yticks([])
#
# plt.subplot(212), plt.imshow(edges2, cmap='gray')
# plt.title('Altered edge'), plt.xticks([]), plt.yticks([])

while(1):
    cv2.imshow('EdgeTest', edges2)

    min = cv2.getTrackbarPos('Min', 'EdgeTest')
    max = cv2.getTrackbarPos('Max', 'EdgeTest')

    edges2 = cv2.Canny(img, min, max)
    k = cv2.waitKey(5)
    if k == 27:
        break

cv2.destroyAllWindows()
#plt.subplot(313), plt.imshow(edges2, cmap='gray')
#plt.title('Edges'), plt.xticks([]), plt.yticks([])
