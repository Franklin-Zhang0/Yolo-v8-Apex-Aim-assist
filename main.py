# take a screenshot and resize it to 1/3 size
import argparse
from screenshots import *
import time
from pynput import mouse, keyboard
from MyListener import listen_key, listen_mouse, get_S_L, Mouse_redirection, Move_Mouse
from predict import *
from args_ import *
from threading import Thread
from multiprocessing import Process, Pipe, Value
from show_target import Show_target

global Start_detection, Listen
# Start listen the right mouse button and the esc
def listeners(Start_detection, Listen):
    # key_listener = keyboard.Listener(on_press=listen_key)
    # key_listener.start()

    mouse_listener = mouse.Listener(on_click=listen_mouse)
    mouse_listener.start()
    print("listener start")
    mouse_listener.join()


if __name__ == "__main__":
    # create a arg set
    Start_detection = Value("b", False)
    Listen = Value("b", True)

    args = argparse.ArgumentParser()
    args = arg_init(args)

    process1 = Thread(
        target=listeners,
        args=(Start_detection, Listen),
    )
    process1.start()

    Mouse_mover = Thread(target=Move_Mouse, args=(args,), name="Mouse_mover")
    Mouse_mover.start()

    print("Main start")
    while Listen:
        Start_detection, Listen = get_S_L()
        if Start_detection:
            # take a screenshot
            take_shots(args)
            # predict the image
            predict_res = predict(args)
            time.sleep(args.wait)
            boxes = predict_res.boxes
            boxes = boxes[boxes[:].cls == args.target_index]
            boxes = boxes[:].xyxy
            if args.show:
                for box in boxes:
                    Show_target(box.numpy() / args.resize)
            if boxes.shape[0] > 0:
                Mouse_redirection(boxes, args)
        else:
            time.sleep(0.1)
            continue

    print("main over")
