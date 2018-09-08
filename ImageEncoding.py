# Ishan Waykul, Shantanu Mantri, Tevon Walker
# Home Depot Hackathon

##File to encode images into 2d arrays

import tensorflow
import numpy
from scipy import ndimage
from scipy import misc
from PIL import Image
import glob
import os

#os.chdir("originalPics/2002/07/19/big")

years = [2002, 2003]

month = [(7, 12), (1,9)]

face = misc.face()
misc.imsave("img_18.jpg", face)

valid_images = [".jpg",".gif",".png",".tga"]
imageArray = []

days_per_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

#print(days_per_month)

#for month in days_per_month:
    #print(days_per_month[month])

#GENERALIZE


day = 1
start = 1

for year in years:
    i = year - 2002
    start = 1
    for m in range(month[i][0], month[i][1]+1):
        month_str = str(m)
        end = days_per_month[m]+1
        if (len(month_str) == 1):
            month_str = "0" + month_str
        if (i == 0 and m == 7):
            start = 19
        if (i == 1 and m == 9):
            end = 3
        for d in range(start, end):
            day_str = str(d)
            if (len(day_str) == 1):
                day_str = "0" + day_str
            currPath = "originalPics/" + str(year) + "/" + month_str + "/" + day_str + "/big/*.jpg"
            for filename in glob.glob(currPath):
                current_img = Image.open(filename)
                imageArray.append(current_img)
                current_img.close()
        start = 1

print(len(imageArray))
#for filename in glob.glob("originalPics/2002/07/19/big/*.jpg"):
    #current_img = Image.open(filename)
    #imageArray.append(current_img)

