import os


def arg_init(args):
    dirpath = os.path.dirname(os.path.realpath(__file__))
    args.add_argument("--dir", type=str, default=dirpath, help="root dir path")
    args.add_argument(
        "--save_dir", type=str, default=dirpath + "/predict", help="save dir"
    )
    args.add_argument(
        "--model_dir", type=str, default=dirpath + "/model", help="model dir"
    )
    args.add_argument("--model", type=str,
                      default="/apex_8n.trt", help="model path")
    args.add_argument("--iou",type=float,
                      default=0.8,help="predict iou")
    args.add_argument("--conf",type=float,
                        default=0.6,help="predict conf")
    args.add_argument("--crop_size", type=float,
                      default=1/2, help="the portion to detect from the screen(=crop_window_height/screen_height)(It's always a rectangle)(from 0 to 1)")
    args.add_argument("--wait", type=float, default=0, help="wait time")
    args.add_argument("--verbos", type=bool, default=False, help="predict verbos")
    args.add_argument("--target_index", type=int,
                      default=1, help="target index")
    args.add_argument("--half", type=bool, default=False,
                      help="use half to predict")
    # args.add_argument("--mouse_speed", type=float,
    #                     default=5., help="mouse speed(mouse sensitivity in the game)")
    args.add_argument("--smooth",type=int,
                      default=5,help="how smooth the mouse move(from 1. to 5.)")
    args.add_argument("--game_fps", type=int, default=60, help="the fps in the game")

    # PID args
    args.add_argument("--pid", type=bool, default=True, help="use pid")
    args.add_argument("--Kp", type=float, default=0.25, help="Kp")
    args.add_argument("--Ki", type=float, default=0.05, help="Ki")
    args.add_argument("--Kd", type=float, default=0.2, help="Kd")

    args = args.parse_args(args=[])
    return args
