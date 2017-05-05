#!/usr/bin/python
# -*- coding: UTF-8 -*-

 #
 # Author: Jianmeng Huang 
 # <jianmenghuang<AT>gmail.com>
 #
 # File: keypoints.py
 # Create Date: 2017-05-05 10:17:24
 #

import numpy as np
import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread('puzzlebox.png',0)          # queryImage
#img1 = cv2.imread('arrowleft',0)          # queryImage
img2 = cv2.imread('Screenshot.png',0) # trainImage
# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
plt.imshow(img3),plt.show()
