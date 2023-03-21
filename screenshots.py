import pyautogui
import argparse
import cv2


def take_shots(args):
    path = args.dir + "/screenshots/screenshot.png"
    pyautogui.screenshot(path)
    img = cv2.imread(path)
    img = cv2.resize(img, (0, 0), fx=args.resize, fy=args.resize)
    cv2.imwrite(path, img)
