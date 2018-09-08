# Ishan Waykul, Shantanu Mantri, Tevon Walker
# Home Depot Hackathon

##File to encode images into 2d arrays

import tensorflow
import numpy as np
from scipy import ndimage
from scipy import misc
from PIL import Image
import glob
import os
import csv
import cv2
import math

os.chdir("ProjectData/lfpw/trainset/")
image_array = []
smallestRes = 10000000
imgId = 0
length = 0
width = 0
for img in range(1, 872):
    full_img_str = "img."
    if (img < 10):
        full_img_str = "image_000" + str(img)+ ".png"
    elif (img < 100):
        full_img_str = "image_00" + str(img) + ".png"
    else:
        full_img_str = "image_0" + str(img) + ".png"
    try:
        im = Image.open(full_img_str)
        cur_res = im.size[0]*im.size[1]
        if (cur_res < smallestRes):
            smallestRes = cur_res
            length = im.size[0]
            width = im.size[1]
            imgId = img
    except:
        pass

print("SMALLEST RES: ", smallestRes)
print("IMG ID: ", imgId)

for img in range(1, 872):
    indiv_img_array = []
    full_img_str = "."
    img_info = "."
    if (img == imgId):
        pass
    else:
        if (img < 10):
            full_img_str = "image_000" + str(img)+ ".png"
            img_info = "image_000" + str(img)+ ".pts"
        elif (img < 100):
            full_img_str = "image_00" + str(img) + ".png"
            img_info = "image_00" + str(img)+ ".pts"
        else:
            full_img_str = "image_0" + str(img) + ".png"
            img_info = "image_0" + str(img)+ ".pts"
        try:
            im = Image.open(full_img_str)
            pic_length_ratio= length/im.size[0]
            pic_width_ratio = width/im.size[1]
            open_pts_file = open(img_info)
            ctr = 0
            for line in open_pts_file.readlines():
                if (ctr > 2 and ctr < 71):
                    coord = line.strip().split(" ")
                    x = int(float(coord[0]) * pic_length_ratio)
                    y = int(float(coord[1]) * pic_width_ratio)
                    indiv_img_array.append((x,y))
                ctr = ctr + 1
                newstr = "RESCALED" + full_img_str
            image_array.append(indiv_img_array)
        except:
            pass
        
print(len(image_array))
