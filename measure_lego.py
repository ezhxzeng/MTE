# import the necessary packages
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import pyzbar.pyzbar as pyzbar
import cv2

# local dependecies
import qr_code
import object_size


# Main
if __name__ == '__main__':
    # Read image
    im_path = input("input image path: ")
    im = cv2.imread(im_path)

    decodedObjects, qr_info = qr_code.decode(im)
    # qr_code.display(im, decodedObjects)

    # Measure 
    if abs(1-(qr_info["width"]/qr_info["height"])) < 0.05:
        object_size.objsize(im, qr_info)
    else:
        print("Image is not aligned")
