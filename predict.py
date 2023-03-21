from ultralytics import YOLO


def predict(args):
    # print("Start detection")
    # print(args.dir + "/yolov8n.pt")
    model = YOLO(args.model_dir + "/yolov8n.pt")
    res = model(
        args.dir + "/screenshots/screenshot.png", verbose=args.verbos, half=args.half
    )
    # print(res)
    return res[0]
