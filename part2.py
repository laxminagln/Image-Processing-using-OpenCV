#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:20:15 2020

@author: nagln
"""

import cv2

cap = cv2.VideoCapture('myvideo.mkv')

#if wrong path
if cap.isOpened() == False:
    print("Error!")
    
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)
        if cv2.waitKey(15) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()