import dxcam
import win32api
camera = dxcam.create()
def take_shots(args):
    #get the screen size
    screen_size = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    center=(screen_size[0]/2,screen_size[1]/2)
    region = (center[0]-screen_size[0]*args.crop_size/2, center[1]-screen_size[1]*args.crop_size/2,
              center[0]+screen_size[0]*args.crop_size/2, center[1]+screen_size[1]*args.crop_size/2)
    region = tuple(map(int, region))
    #print(region)
    img= camera.grab(region=region)
    return img