from ultralytics import YOLO

def predict_init(args):
    global model
    print("Predict on", args.model_dir + args.model)
    model = YOLO(args.model_dir + args.model)
def predict(args,img):
    global model
    if img is None: 
        res = model(
            args.dir + "/screenshots/screenshot.png", verbose=args.verbos, half=args.half, iou=0.7
        )
    else:
        res = model(img, verbose=args.verbos, half=args.half, iou=0.7)
    #print(res)
    return res[0]
