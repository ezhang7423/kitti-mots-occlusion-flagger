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
    for x in range(len(boxes)):
        box = [i for i in boxes[x]]
        print(len(box))
        
    return;

def returnBoxes(frame):
    frame128 = frame
    bBoxes = []
    for x in range(len(frame128)):
        if (frame128[x].class_id == 1 or frame128[x].class_id == 1):
            bBoxes.append(rletools.toBbox(frame128[x].mask))
    return bBoxes

if __name__ == "__main__":
    frames = load_txt("instance_sample.txt")
    occlusions = []
    # for x in range(len(frames)):
    occlusions.append(isOccluded(returnBoxes(frames[x])))

    

