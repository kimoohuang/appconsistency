#!/usr/bin/python
# -*- coding: UTF-8 -*-

 #
 # Author: Jianmeng Huang 
 # <jianmenghuang<AT>gmail.com>
 #
 # File: try.py
 # Create Date: 2017-04-28 15:36:12
 #
import os
import numpy as np
from scipy import signal
from scipy import misc

#print os.getcwd()
#needle = misc.imread(os.path.join(os.getcwd(),'arrowleft.png'))
needle = misc.imread('arrowleft.png','L')
haystack = misc.imread('Screenshot.png','L')
print needle
# print needle.shape
# print haystack.shape
# print haystack
#haystack = haystack + np.random.randn(*haystack.shape) * 50

# corr = signal.correlate2d(haystack, needle, boundary='symm', mode='same')
# y, x = np.unravel_index(np.argmax(corr), corr.shape)  # find the match
# print y, x
#
# import matplotlib.pyplot as plt
# fig, (ax_orig, ax_template, ax_corr) = plt.subplots(3, 1, figsize=(6, 15))
# ax_orig.imshow(haystack, cmap='gray')
# ax_orig.set_title('Original')
# ax_orig.set_axis_off()
# ax_template.imshow(needle, cmap='gray')
# ax_template.set_title('Template')
# ax_template.set_axis_off()
# ax_corr.imshow(corr, cmap='gray')
# ax_corr.set_title('Cross-correlation')
# ax_corr.set_axis_off()
# ax_orig.plot(x, y, 'ro')
# fig.show()
# fig.savefig("temp.png", dpi=None, facecolor='w', edgecolor='w',
#                   orientation='portrait', papertype=None, format=None,
#                   transparent=False, bbox_inches=None, pad_inches=0.1,
#                   frameon=None)