import picamera
import time

path = '/home/pi/src5/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640,480)
    camera.start_preview()
    time.sleep(3)
    
    while(1):
        now_str = time.strftime("%Y%m%d_%H%M%s")
        a = input("1. Picture 2. Video 3. Exit\n")
        if a==1:
            camera.capture('%s/photo_%s.jpg'.format(path,now_str))
        elif a==2:
            camera.start_recording('%s/video_%s.h264'.format(path,now_str))
            b = input("Press any Key to stop recording...\n")
            camera.stop_recording()
        else :
            break

finally:
    camera.stop_preview()