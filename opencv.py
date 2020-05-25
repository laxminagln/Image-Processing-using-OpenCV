#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:45:33 2020

@author: nagln
"""

import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

output = cv2.VideoWriter('myvideo.mkv',
                         cv2.VideoWriter_fourcc(*'XVID'),
                         20,
                         (width, height))

while True:
    ret, frame = cap.read()
    
    output.write(frame)
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame',gray)
    cv2.imshow('frame',frame)
    #27 == esc button
    if cv2.waitKey(5) & 0xFF == 27:
        break
    
cap.release()
output.release()
cv2.destroyAllWindows()
