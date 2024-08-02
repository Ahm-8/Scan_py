#importing packages
from skimage.filters import threshold_local                     # For resizing, rotating and cropping images 
import numpy as np
import argparse
import cv2
import imutils


def order_points(pts):
    rect = np.zeros((4,2), dtype = "float32")

    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmin(s)]

    diff = np.diff(pts,axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmin(diff)]

    return rect

def four_point_transform(image,pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # Find the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0] ** 2) + (br[1] - bl[1] ** 2)))
    widthB = np.sqrt(((tr[0] - tl[0] ** 2) + (tr[1] - tl[1] ** 2)))
    maxWidth = max(int(widthA), int(widthB))

    # Doing the same as above for height
    heightA =  np.sqrt(((tr[0] - br[0] ** 2) + (tr[1] - br[1] ** 2)))
    heightB =  np.sqrt(((tl[0] - bl[0] ** 2) + (tl[1] - bl[1] ** 2)))
    maxHeight = max(int(heightA), int(heightB))

    # Constructing Birds Eye View after getting the dimensions of the new image

    dst = np.array([
        [0,0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    
    # Compute the prespective transform matrix and then apply it

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped                   

    