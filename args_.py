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
    args.add_argument("--resize", type=float, default=1 / 5, help="resize image")
    args.add_argument("--wait", type=float, default=0, help="wait time")
    args.add_argument("--verbos", type=bool, default=True, help="verbos")
    args.add_argument("--target_index", type=int, default=0, help="target index")
    args.add_argument("--half", type=bool, default=True, help="use half to predict")
    args.add_argument("--mouse_speed", type=float, default=1, help="mouse speed base")
    args = args.parse_args(args=[])
    return args
