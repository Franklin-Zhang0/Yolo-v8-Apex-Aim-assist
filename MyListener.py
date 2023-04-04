from pynput import mouse, keyboard
import numpy as np
import pyautogui
import time
import win32api

Start_detection = False
Listen = True
destination = np.array([-1, -1])
width = 0
interval = 0.01
mouse_instance = mouse.Controller()
screen_size = np.array([win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)])
screen_center=(screen_size[0]/2,screen_size[1]/2)


def get_S_L():
    global Start_detection
    global Listen
    return Start_detection, Listen


# if the esc is clicked, return True
def listen_key(key):
    if key == keyboard.Key.home:
        global Start_detection
        global Listen
        Listen = False
        Start_detection = False
        print("Stop listening")


# if the right mouse is clicked, return True
def listen_mouse(x, y, button, pressed):
    global Start_detection
    if button == mouse.Button.right:
        if pressed:
            Start_detection = not Start_detection
            print("Start detection: ", Start_detection)

def speed_func(x, speed, smooth):
    return max(speed*x/smooth/2, 1.)

def Move_Mouse(args):
    global screen_size,screen_center
    region = (screen_center[0]-screen_size[0]*args.crop_size/2, screen_center[1]-screen_size[1]*args.crop_size/2,
              screen_center[0]+screen_size[0]*args.crop_size/2, screen_center[0]+screen_size[1]*args.crop_size/2)
    while Listen:
        global destination, width, interval, mouse_instance
        if Start_detection:
            pos = np.array(mouse_instance.position)
            mouse_vector = destination - pos
            norm = np.linalg.norm(mouse_vector)
            #if destination not in region
            if norm < max(width/6,5) or destination[0] < region[0] or destination[0] > region[0]+region[2] or destination[1] < region[1] or destination[1] > region[1]+region[3]:
                destination[0] = -1
                time.sleep(0.01)
                continue

            # normalize mouse_vector
            normalized_vector = mouse_vector * 1.0 / norm
            mouse_vector = normalized_vector

            # mouse_instance.position = tuple(
            #     pos + mouse_vector * speed_func(norm, args.mouse_speed, args.smooth)
            # )
            # time.sleep(interval/args.smooth)
            des=pos+mouse_vector*speed_func(norm, args.mouse_speed, args.smooth)
            pyautogui.moveTo(des[0],des[1], interval/args.smooth)
        else:
            time.sleep(0.01)
            continue


# redirect the mouse closer to the nearest box center
def Mouse_redirection(boxes, args, tpf):
    global destination, width, interval, mouse_instance, screen_size
    interval = tpf
    pos = np.array(mouse_instance.position)

    # Get the center of the boxes
    boxes_center = (
        (boxes[:, :2] + boxes[:, 2:]) / 2
    )
    boxes_center[:, 1] = (
        boxes[:, 1] * 0.9 + boxes[:, 3] * 0.1
    )
    # Map the box from the image coordinate to the screen coordinate
    screen_center = screen_size / 2
    start_point = screen_center- screen_size * args.crop_size / 2
    boxes_center[:, 0] = boxes_center[:, 0] + start_point[0]
    boxes_center[:, 1] = boxes_center[:, 1] + start_point[1]

    # Find the nearest box center
    dis = np.linalg.norm(boxes_center - pos, axis=-1)
    min_index = np.argmin(dis)
    width = boxes[min_index, 2] - boxes[min_index, 0]
    destination = boxes_center[np.argmin(dis)]
    #print(destination)

    # mouse_instance.position = tuple(boxes_center[np.argmin(dis)])
