# -*- coding: utf-8 -*-
import subprocess
import picamera
import os
from time import sleep

shutter_numb = 0
photo_dir = os.path.expanduser('~/denpa-gardening/photo_data')

def cameraLoad():
    global shutter_numb
    filename = os.path.join(photo_dir, 'camera.set')
    try:
        fp = open(filename)
        tmp_shutter_numb = fp.readlines()
        tmp2_shutter_numb = tmp_shutter_numb[0].rstrip()
        shutter_numb = int(tmp2_shutter_numb)
        fp.close()
    except IOError:
        print 'no camera.set data, make set files'

def cameraSave():
    filename = os.path.join(photo_dir, 'camera.set')
    fp = open(filename, 'w')
    fp.write(str(shutter_numb))
    fp.close()

def shutter():
    global shutter_numb
    shutter_numb +=1

    filename = os.path.join(photo_dir, str("{0:06d}".format(shutter_numb)) + '.jpg')
    photofile = open(filename, 'wb')
    print(photofile)

    with picamera.PiCamera() as camera:
        camera.resolution = (2592,1944)
        camera.start_preview()
        sleep(1.000)
        camera.capture(photofile)

    photofile.close()

if __name__ == '__main__':
    cmd ="sudo killall mjpg_streamer"
    subprocess.call(cmd, shell=True)

    cameraLoad()
    shutter()
    cameraSave()

    cmd = "stream.sh"
    subprocess.call(cmd, shell=True)
