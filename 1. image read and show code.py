# a snippet to read an image and to display it

import numpy as np
import cv2

img = cv2.imread('address of file',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
