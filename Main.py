


import cv2
import numpy as np

import os

import glob

vidcap = cv2.VideoCapture('F:/RCNN/Group4_RCNN/Crowd.mp4')
success,image = vidcap.read()
count = 0
while success:
      image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
      cv2.imwrite('C:/Users/hasan/OneDrive/Desktop/Research/ExtFrame'+ "\\frame%d.jpg" % count, image)   # save frame as JPEG file      
      success,image = vidcap.read()
      print('Read a new frame: ', success)
  
      count += 1
  
print ('The no. of frames',count)







