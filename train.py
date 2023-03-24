from ultralytics import YOLO
from args_ import *
import argparse

# Train YOLOv5s on dataset for 100 epochs
def train(args):
    model = YOLO("yolov8n.pt")
    model.train(data=args.dir + "/dataset/data.yaml", epochs=20)
    model.val()


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args = arg_init(args)
    train(args)
