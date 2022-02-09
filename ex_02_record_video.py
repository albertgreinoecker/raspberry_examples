from picamera import PiCamera
from time import sleep

camera = PiCamera()
'''
Es gelten die gleichen Einstellungen wie in Beispiel 01
'''


'''
Ein Video wird für 5 Sekunden aufgenommen
'''
camera.start_recording('/home/pi/video.h264')
sleep(5)
camera.stop_recording()
