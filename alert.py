#!/usr/bin/python3
# -*-coding:UTF-8 -*
"""
    pour le moment, je bidouille avec ce script mais il va falloir
    faire plus sophistique
"""

import picamera
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

print('Appuyez sur le bouton pour allumer appareil photo')
GPIO.wait_for_edge(17, GPIO.FALLING)
print('Merci')

with picamera.PiCamera() as camera:
#    camera.vflip = True
#    camera.hflip = True
#    camera.start_preview()

    frame = 1
    while True:
        print('Appuyez sur le bouton pour prendre une photo')
        GPIO.wait_for_edge(17, GPIO.FALLING)
        print('Merci')
        camera.capture('./animation/alerte%03d.jpg' % frame)
        frame += 1

#    camera.stop_preview()
