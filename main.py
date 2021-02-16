import numpy as np
import cv2
import pyautogui

xStart = 1600
xSize = 320
yStart = 900
ySize = 180
waitTime = 1000
while(True):
    img = pyautogui.screenshot(region=(xStart,yStart, xSize, ySize))
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    dim = (4*xSize,4*ySize)
    cv2.imshow('test',cv2.resize(frame, dim, interpolation = cv2.INTER_AREA))
    cv2.waitKey(waitTime)