import picamera
import time

path = '/home/pi/src5/06_multimedia'

camera = picamera.PiCamera()
num = 0

try:
    camera.resolution = (640,480)
    camera.start_preview()
    time.sleep(3)

    while(1):
        num = int(input("1. Photo  2. Video  3. Exit\n >>"))

        if num == 1 :
            print("Camera\n")
            now_str=time.strftime("%Y%m%d_%H%M%S")
            camera.capture('%s/photo_%s.jpg'%(path,now_str))

        elif num == 2 :
            print("Video\n")
            now_str=time.strftime("%Y%m%d_%H%M%S")
            camera.start_recording('%s/video_%s.h264' %(path,now_str))
            time.sleep(10)
            camera.stop_recording()
        else:
            print("Exit\n")
            break
finally:
    camera.stop_preview()
    