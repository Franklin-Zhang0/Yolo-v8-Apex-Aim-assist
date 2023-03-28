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
def listeners():
    # key_listener = keyboard.Listener(on_press=listen_key)
    # key_listener.start()

    mouse_listener = mouse.Listener(on_click=listen_mouse)
    mouse_listener.start()
    print("listener start")
    mouse_listener.join()


if __name__ == "__main__":
    # create a arg set
    Listen=True

    args = argparse.ArgumentParser()
    args = arg_init(args)

    process1 = Thread(
        target=listeners,
        args=(),
    )
    process1.start()

    Mouse_mover = Thread(target=Move_Mouse, args=(args,), name="Mouse_mover")
    Mouse_mover.start()

    predict_init(args)
    print("Main start")
    while Listen:
        time_start = time.time()
        Start_detection, Listen = get_S_L()
        # take a screenshot
        img=take_shots(args)
        #print("shots time: ", time.time() - time_start)
        # predict the image
        predict_res = predict(args,img)
        #print("shot+predict time: ", time.time() - time_start)
        time.sleep(args.wait)
        boxes = predict_res.boxes
        boxes = boxes[boxes[:].cls == args.target_index]
        boxes = boxes.cpu()
        boxes = boxes[:].xyxy
        
        if Start_detection:
            if boxes.shape[0] > 0:
                Mouse_redirection(boxes, args)
        print("total time: ", time.time() - time_start)
        

    print("main over")
