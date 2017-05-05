#!/usr/bin/python
# -*- coding: UTF-8 -*-

 #
 # Author: Jianmeng Huang 
 # <jianmenghuang<AT>gmail.com>
 #
 # File: try2.py
 # Create Date: 2017-04-30 17:04:41
 #

import cv2
import numpy as np
image = cv2.imread("Screenshot.png")
template = cv2.imread("backbutton.png")
# print template
# print template.shape
# print template[0,...]
# print template[...,0]
# print template[...,1]
# print template[...,2]
# print template.shape[-1]
# for i in range(template.shape[-1]):
#     print i
#     print template[...,i]

for x in range(template.shape[0]):
    for y in  range(template.shape[1]):
        for z in range(template.shape[2]):
             if template[x,y,z] == 255 :
                 template[x,y,z] =0
for i in range(template.shape[-1]):
    print i
    print template[...,i]

print image.shape
result = cv2.matchTemplate(image,template,cv2.TM_CCORR_NORMED)
print np.unravel_index(result.argmax(),result.shape)
