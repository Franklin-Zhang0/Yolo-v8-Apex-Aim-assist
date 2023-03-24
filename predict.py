from ultralytics import YOLO


def predict(args):
    print("Predict on", args.model_dir + args.model)
    model = YOLO(args.model_dir + args.model)
    # model = YOLO(args.dir + "/runs/detect/train2/weights/best.pt")
    res = model(
        args.dir + "/screenshots/screenshot.png", verbose=args.verbos, half=args.half
    )
    print(res)
    return res[0]
