from cvlearn import HandTrackingModule as handTracker

import cv2
cap = cv2.VideoCapture(0)
detector = handTracker.handDetector()
while True:
    ret, img = cap.read()
    img = detector.findHands(img)

    cv2.imshow("Result", img)
    cv2.waitKey(1)