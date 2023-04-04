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
                      default="/apex_total_8n_350_1000.pt", help="model path")
    args.add_argument("--crop_size", type=float,
                      default=1/2, help="the portion to detect from the screen(from 0 to 1)")
    args.add_argument("--wait", type=float, default=0, help="wait time")
    args.add_argument("--verbos", type=bool, default=False, help="verbos")
    args.add_argument("--target_index", type=int,
                      default=0, help="target index")
    args.add_argument("--half", type=bool, default=False,
                      help="use half to predict")
    args.add_argument("--mouse_speed", type=float,
                        default=3., help="mouse speed(from 1 to 10, too high may cause difficult it to coordinate)")
    args.add_argument("--smooth",type=float,
                      default=2.,help="how smooth the mouse move(from 1. to 5.)")
    args = args.parse_args(args=[])
    return args
