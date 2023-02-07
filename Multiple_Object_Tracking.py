import sys
from random import randint

import cv2

tracker_types = ["BOOSTING", "MIL", "KCF", "TLD", "MEDIANFLOW", "MOOSE", "CSRT"]

def create_tracker_by_name(tracker_type):

    if tracker_type == "BOOSTING":
        tracker = cv2.legacy.TrackerBoosting_create()
    elif tracker_type == "MIL":
        tracker = cv2.legacy.TrackerMIL_create()
    elif tracker_type == "KCF":
        tracker = cv2.legacy.TrackerKCF_create()
    elif tracker_type == "TLD":
        tracker = cv2.legacy.TrackerTLD_create()
    elif tracker_type == "MEDIANFLOW":
        tracker = cv2.legacy.TrackerMedianFlow_create()
    elif tracker_type == "MOSSE":
        tracker = cv2.legacy.TrackerMOSSE_create()
    elif tracker_type == "CSRT":
        tracker = cv2.legacy.TrackerCSRT_create()
    else :
        print("Invalid Tracker Name. Valid Trackers are : ")
        for t in tracker_types:
            print(t)

video = cv2.VideoCapture("videos/race.mp4")
if not video.isOpened():
    print("Error while loading the video")
    sys.exit()

ok,frame = video.read()

bboxes = []
colors = []

while True :

    bbox = cv2.selectROI(frame)
    bboxes.append(bbox)
    colors.append((randint(0,255), randint(0,255), randint(0,255)))

    print("Press Q to Quit and start tracking")
    print("Press any other key to select the next object")

    k = cv2.waitKey(0) & 0XFF
    if k == 113:
        break