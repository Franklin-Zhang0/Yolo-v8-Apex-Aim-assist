from pynput import mouse, keyboard
import numpy as np
import time

Start_detection = False
Listen = True
destination = np.array([-1, -1])


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
    time.sleep(0.3)


# if the right mouse is clicked, return True
def listen_mouse(x, y, button, pressed):
    global Start_detection
    if button == mouse.Button.middle:
        if pressed:
            Start_detection = not Start_detection
            print("Start detection: ", Start_detection)
    time.sleep(0.3)


def Move_Mouse(args):
    while Listen:
        if Start_detection:
            global destination
            mouse_instance = mouse.Controller()
            pos = np.array(mouse_instance.position)
            mouse_vector = destination - pos
            norm = np.linalg.norm(mouse_vector)
            if norm < 5 or destination[0] < 0:
                destination[0] = -1
                time.sleep(0.005)
                continue

            # normalize mouse_vector
            normalized_vector = mouse_vector * 1.0 / norm
            mouse_vector = normalized_vector * np.log(norm)

            mouse_instance.position = tuple(
                pos + mouse_vector * args.mouse_speed
            )  # +0.1*np.random(2)*(np.linalg.norm(mouse_vector))
            time.sleep(0.005)
        else:
            continue


# redirect the mouse closer to the nearest box center
def Mouse_redirection(boxes, args):
    global destination
    mouse_instance = mouse.Controller()
    pos = np.array(mouse_instance.position)

    # print(boxes.shape, type(boxes.numpy()))
    boxes_center = (
        np.array(boxes.numpy()[:, :2] + boxes.numpy()[:, 2:]) / 2 / args.resize
    )
    boxes_center[:, 1] = (
        boxes.numpy()[:, 1] * 0.9 + boxes.numpy()[:, 3] * 0.1
    ) / args.resize
    dis = np.linalg.norm(boxes_center - pos, axis=-1)

    destination = boxes_center[np.argmin(dis)]

    # mouse_instance.position = tuple(boxes_center[np.argmin(dis)])
