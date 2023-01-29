from picamera import PiCamera  # Achtung! Diese Bibliothek gibt es nur am Raspberry
from time import sleep


camera = PiCamera()

'''
Grundlegende Einstellungen für die Kamera
Weitere Einstellungen sind unter https://picamera.readthedocs.io/en/release-1.13/api_camera.html zu finden.
'''
#camera.resolution = (1024, 768)
camera.rotation = 0 # 90, 180, 270 grad
camera.framerate = 15 # Frames pro Sekunde (FPS)
'''
Die Preview macht nur ein Sinn, wenn man einen Monitor angehängt hat bzw. mit VNC verbunden ist
'''
#camera.start_preview()

sleep(5) # Ein wenig warten, damit sich die Kamera bezgl. Licht einpendelt
'''
Bild aufnehmen
Folgende Parameter machen da Sinn:
* alpha : zwischen 0 und 255
* resize=(320, 240)
'''
camera.capture('/home/pi/image.jpg')
 #camera.stop_preview()