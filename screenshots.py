import dxcam
import win32api
import time

camera = dxcam.create()
region = None
def shot_init(args):
    global region, camera
    screen_size = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    center=(screen_size[0]/2,screen_size[1]/2)
    region = (center[0]-screen_size[1]*args.crop_size/2, center[1]-screen_size[1]*args.crop_size/2,
                center[0]+screen_size[1]*args.crop_size/2, center[1]+screen_size[1]*args.crop_size/2)
    region = tuple(map(int, region))
    #camera.start(target_fps=args.game_fps, region=region)
def take_shots(args):
    global region, camera
    # camera.get_latest_frame()
    # camera.get_latest_frame()
    # img= camera.get_latest_frame()
    img=camera.grab(region=region)
    return img