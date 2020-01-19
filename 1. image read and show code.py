# a snippet to read an image and to display it

import numpy as np
import cv2

img = cv2.imread('address of file',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# description
# The import keyword is used to import library
# a variable 'img' is stored with an image specified through the address. The function used is 'imread()'
# 0 value refers to gray and 1 refers to color
