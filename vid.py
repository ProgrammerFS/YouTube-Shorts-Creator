import os

import cv2
import numpy as np
import glob

def make_video():
    img_array = []
    for filename in glob.glob('./*.jpg'):
        img = cv2.imread(filename)
        for i in range(170):
            img_array.append(img)

    out = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'DIVX'),30, (1200, 1500))

    for i in range(len(img_array)):
        rgb_img = cv2.cvtColor(img_array[i], cv2.COLOR_RGB2BGR)
        out.write(rgb_img)
    out.release()
    print("file saved")

    for filename in glob.glob('./*.jpg'):
        os.remove(filename)