# take a screenshot and resize it to 1/3 size
import argparse
from screenshots import *
import time
from pynput import mouse, keyboard
from keyboard import listen_key, listen_mouse, get_S_L, Mouse_redirection, Move_Mouse
from predict import *
from args_ import *
from threading import Thread
from multiprocessing import Process, Pipe

global Start_detection, Listen
# Start listen the right mouse button and the esc
def listeners(pipe1, pipe2):
    Start_detection = False
    Listen = True
    key_listener = keyboard.Listener(on_press=listen_key)
    key_listener.start()

    mouse_listener = mouse.Listener(on_click=listen_mouse)
    mouse_listener.start()
    while 1:
        tmp1, tmp2 = get_S_L()
        if tmp1 != Start_detection or tmp2 != Listen:
            print("Send!")
            Start_detection = tmp1
            Listen = tmp2
            # pipe1.send(Start_detection)
            # pipe2.send(Listen)
        time.sleep(0.1)
        continue


if __name__ == "__main__":
    # create a arg set
    Start_detection = False
    Listen = True
    (pipe1, pipe2) = Pipe()

    args = argparse.ArgumentParser()
    args = arg_init(args)

    process1 = Thread(
        target=listeners,
        args=(pipe1,pipe2,),
    )
    process1.start()
    Mouse_mover = Thread(target=Move_Mouse, args=(args,), name="Mouse_mover")
    Mouse_mover.start()
    cnt = 0
    print("Right click to start listening...")
    while Listen:
        # Start_detection = pipe1.recv()
        # Listen = pipe2.recv()
        Start_detection, Listen = get_S_L()
        # print("Main Start_detection: ", Start_detection)
        # print("Main Listen: ", Listen)
        if Start_detection:
            # take a screenshot
            take_shots(args)
            # predict the image
            predict_res = predict(args)
            # print("#", end=" ")
            # wait 1 second
            time.sleep(args.wait)
            boxes = predict_res.boxes
            boxes = boxes[boxes[:].cls == args.target_index]
            boxes = boxes[:].xyxy
            if boxes.shape[0] > 0:
                Mouse_redirection(boxes, args)

    # key_listener.stop()
    # mouse_listener.stop()
    print("main over")
