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

# open source image
originalImage = cv2.imread('image.png')

# convert image to grayscale
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

# convert image to black and white
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

# uncomment below lines to preview image
cv2.imshow('Black & white image', blackAndWhiteImage)  
cv2.waitKey(0)
cv2.destroyAllWindows()

# global coordinates of where to start drawing (change if needed!)
x_start = 250
y_start = 150

# wait before user clicks on window to within
time.sleep(5)

# put mouse mointer into initial position
pg.moveTo(x_start, y_start)

# get row indexes
random_rows = list(range(len(blackAndWhiteImage)))

# comment two lines below if you want a "printer" like behavior
random_rows = random.sample(range(len(blackAndWhiteImage)), len(blackAndWhiteImage))
random.shuffle(random_rows)

# loop over pixel rows
for y in random_rows:
    # randomize cols traversal order
    row = blackAndWhiteImage[y]
    random_cols = list(range(len(row)))
    random.shuffle(random_cols)
    
    # loop over pixel cols
    for x in random_cols:
        if row[x] == 0:
            # draw pixel!
            pg.click(x_start + x, y_start + y, _pause=False)
            print('Drawing at:', x_start + x, y_start + y)
            
            # animation speed
            time.sleep(0.008)

