from typing import Counter
import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")

min_height_rectangle = 50
min_width_rectangle = 50

subs = cv2.bgsegm.createBackgroundSubtractorMOG()
# subs = cv2.createBackgroundSubtractorMOG2()


countLinePos = 550


def center_handle(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


detect = []
offset = 6
Counter = 0

while True:
    ret, frame = cap.read()

    # fgMask = subs.apply(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3, 3), 5)
    img_sub = subs.apply(blur)
    dilate = cv2.dilate(img_sub, np.ones((5, 5)))
    kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilate_ada = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernal)
    dilate_ada = cv2.morphologyEx(dilate_ada, cv2.MORPH_CLOSE, kernal)

    # ret, thres = cv2.threshold(
    #     dilate_ada, 127, 255, cv2.THRESH_BINARY)
    # canny_edge = cv2.Canny(thres, 100, 200)
    contours, h = cv2.findContours(
        dilate_ada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame, (0, countLinePos),
             (1300, countLinePos), (255, 225, 255), 2)

    for (i, c) in enumerate(contours):
        x, y, w, h = cv2.boundingRect(c)

        validate_counter = (w >= min_width_rectangle) and (
            h >= min_height_rectangle)

        if not validate_counter:
            continue

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame, center, 1, (255, 255, 255), -1)

        for (x, y) in detect:
            # if y < (countLinePos + offset) and y > (countLinePos - offset):
            if y < (countLinePos + offset) and y > (countLinePos - offset):
                Counter += 1

                cv2.line(frame, (0, countLinePos),
                         (800, countLinePos), None, 1)
                detect.remove((x, y))
                print("VEHICLE COUNT: " + str(Counter))

    cv2.putText(frame, "VEHICLE COUNT: " + str(Counter), (450, 70),
                cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 2)

    cv2.imshow("Substractor", dilate_ada)
    cv2.imshow("Frame", frame)
    # cv2.imshow("Frame", blur)
    # cv2.imshow("Frame", gray)
    # cv2.imshow("Frame", dilate)
    # cv2.imshow("Frame", subs)
    # cv2.imshow("Frame", contours)

    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()
