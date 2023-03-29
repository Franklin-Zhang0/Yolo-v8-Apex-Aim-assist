import pyautogui
import cv2
import numpy as np
import dxcam

camera = dxcam.create()
def take_shots(args):
    #path = args.dir + "/screenshots/screenshot.png"

    #img=pyautogui.screenshot()
    img= camera.grab()
    
    #img = cv2.resize(img, (0, 0), fx=args.resize, fy=args.resize)
    return img