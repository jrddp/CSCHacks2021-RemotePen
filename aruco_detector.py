import cv2
import cv2.aruco as aruco
import itertools
import numpy as np
import os

aruco_marker_size = 6
aruco_dict_size = 50


# returns (bboxs, ids, reject) of aruco tags found in img
def findArucoMarkers(img):
    # generate grayscale of image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # initialize aruco dictionary and parameters
    key = getattr(aruco, f'DICT_{aruco_marker_size}X{aruco_marker_size}_{aruco_dict_size}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()

    # return detected markers
    return aruco.detectMarkers(gray, arucoDict, parameters=arucoParam)


def get_bbox_centers(bboxs):
    return [find_bbox_center(bbox) for bbox in bboxs]


# where bbox is a [4][2] numpy array containing corner points
def find_bbox_center(bbox):
    # return sum(bbox) / len(bbox)
    # TODO figure out why bbox is 3D to begin with?
    bbox = bbox[0]
    x_points = [point[0] for point in bbox]
    y_points = [point[1] for point in bbox]
    x_center = sum(x_points) / len(x_points)
    y_center = sum(y_points) / len(y_points)
    return (x_center, y_center)


# returns the middle-point between the min/max of each dimension
def find_center_of_all_bboxs(bboxs):
    # min, max x
    x_range = None
    y_range = None

    for bbox in bboxs:
        for sub_bbox in bbox:
            for x, y in sub_bbox:
                if x_range is None:
                    x_range = [x, x]
                    y_range = [y, y]
                    continue

                x_range[0] = min(x_range[0], x)
                x_range[1] = max(x_range[1], x)
                y_range[0] = min(y_range[0], y)
                y_range[1] = max(y_range[1], y)

    if x_range is None:
        return None

    x_center = (x_range[1] + x_range[0]) / 2
    y_center = (y_range[1] + y_range[0]) / 2
    return (x_center, y_center)
