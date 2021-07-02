##########################################
#
#  Simple script to automate the process
#       of drawing using Python
#
#                 by
#
#          Code Monkey King
#
##########################################


# packages
import cv2
import pyautogui as pg
import time
import random

# wait before user clicks on window to within
time.sleep(5)

# global coordinates of where to start drawing (change if needed!)
x_start = 200
y_start = 200

# put mouse mointer into initial position
pg.moveTo(x_start, y_start)

# number of images
frames = 12

# loop over images
for i in range(1, frames + 1):
    # open source image
    originalImage = cv2.imread('./bulk/image' + str(i) + '.png')

    # convert image to grayscale
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

    # convert image to black and white
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

    # uncomment below lines to preview image
    #cv2.imshow('Black & white image', blackAndWhiteImage)  
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # loop over pixel rows
    for y in range(len(blackAndWhiteImage)):
        # init row
        row = blackAndWhiteImage[y]
        
        # loop over pixel cols
        for x in range(len(row)):
            if row[x] == 0:
                # draw pixel!
                pg.click(x_start + x, y_start + y, _pause=False)
                print('Drawing at:', x_start + x, y_start + y)
                
                # animation speed
                time.sleep(0.008)

