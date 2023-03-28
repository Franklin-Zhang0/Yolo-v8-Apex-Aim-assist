import pyautogui
import cv2
import numpy as np

def take_shots(args):
    path = args.dir + "/screenshots/screenshot.png"

    img=pyautogui.screenshot()
    img=np.array(img)
    
    img = cv2.resize(img, (0, 0), fx=args.resize, fy=args.resize)
    return img