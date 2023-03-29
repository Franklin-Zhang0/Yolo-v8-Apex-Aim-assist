from pynput import mouse, keyboard
import numpy as np
import pyautogui
import time

Start_detection = False
Listen = True
destination = np.array([-1, -1])
width = 0
interval = 0.01


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

def speed_func(x, speed):
    if np.abs(x) < speed*3:
        return min(speed/2, x)
    else:
        return speed
def Move_Mouse(args):
    global destination, width, interval
    while Listen:
        if Start_detection:
            mouse_instance = mouse.Controller()
            pos = np.array(mouse_instance.position)
            mouse_vector = destination - pos
            norm = np.linalg.norm(mouse_vector)
            if norm < width/5 or norm >600 or destination[0] < 0:
                destination[0] = -1
                time.sleep(0.001)
                continue

            # normalize mouse_vector
            normalized_vector = mouse_vector * 1.0 / norm
            mouse_vector = normalized_vector

            mouse_instance.position = tuple(
                pos + mouse_vector * speed_func(norm, args.mouse_speed*interval*1000)
            )
            time.sleep(interval)
        else:
            time.sleep(0.001)
            continue


# redirect the mouse closer to the nearest box center
def Mouse_redirection(boxes, args, tpf):
    global destination, width, interval
    interval = tpf
    mouse_instance = mouse.Controller()
    pos = np.array(mouse_instance.position)

    # print(boxes.shape, type(boxes()))
    boxes_center = (
        (boxes[:, :2] + boxes[:, 2:]) / 2 / args.resize
    )
    boxes_center[:, 1] = (
        boxes[:, 1] * 0.9 + boxes[:, 3] * 0.1
    ) / args.resize
    dis = np.linalg.norm(boxes_center - pos, axis=-1)
    min_index = np.argmin(dis)
    width = boxes[min_index, 2] - boxes[min_index, 0]
    if dis[min_index] <width/5:
        destination[0]=-1
        return
    else:
        destination = boxes_center[np.argmin(dis)]

    # mouse_instance.position = tuple(boxes_center[np.argmin(dis)])
