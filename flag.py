import sys
import os
import colorsys
sys.path.insert(0, r"C:\Users\Victor\Desktop\resarch\cocoapi\PythonAPI")

import numpy as np
import matplotlib.pyplot as plt
import pycocotools.mask as rletools
from iot import load_sequences, load_seqmap, load_txt



# def decoded_object(segobject):
#     decoded = rletools.decode(segobject)
#     for x in range(len(decoded)):
#         for y in range(len(decoded[x])):
#             if (decoded[x][y] != 0):
#                 #do something here
#     return;


def isOccluded(boxes):
    x0 = []
    xf = []
    y0 = []
    yf = []
    for x in range(len(boxes)):
        box = [i for i in boxes[x]]
        # x0 += [box[0]] move this to bottom of function
        # xf += [box[2]]
        x_index = [box[0], box[2]]
        for i in range(len(x0)):
            if x0[i] <= x_index[0] <= xf[i]:
                return True
            elif x0[i] <= x_index[1] <= xf[i]:
                return True
        x0.append(x_index[0])
        xf.append(x_index[1])

        y_index = [box[1], box[3]]
        for i in range(len(y0)):
            if y0[i] <= y_index[0] <= yf[i]:
                return True
            elif y0[i] <= y_index[1] <= yf[i]:
                return True
        y0.append(y_index[0])
        yf.append(y_index[1])
        # check if collision
    return False;


def returnBoxes(frame):
    frame128 = frame
    bBoxes = []
    for x in range(len(frame128)):
        if (frame128[x].class_id == 1 or frame128[x].class_id == 2):
            bBoxes.append(rletools.toBbox(frame128[x].mask))
    return bBoxes

if __name__ == "__main__":
    frames = load_txt("instance_sample.txt")
    occlusions = []
    for x in range(len(frames)):
        occlusions.append(isOccluded(returnBoxes(frames[x])))
    print(occlusions)

    

