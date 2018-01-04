# face detection using Haar cascade classifier

# Face detection works by using the Haar Cascade feature detector on an image. A
# Haar Cascade is a series of simple area contrasts checks. For the built-in
# frontalface detector there are 25 stages of checks with each stage having
# hundreds of checks a piece. Haar Cascades run fast because later stages are
# only evaluated if previous stages pass. Additionally, your OpenMV Cam uses
# a data structure called the integral image to quickly execute each area
# contrast check in constant time (the reason for feature detection being
# grayscale only is because of the space requirment for the integral image).

# By: yuanz - Dec 26 2017
# reference: openmv.io

import sensor, time, image

#Initializes the camera sensor
sensor.reset()

#Set the camera image contrast. -3 to +3
sensor.set_contrast(1)
#Set the camera image gainceiling. 2, 4, 8, 16, 32, 64, or 128.
sensor.set_gainceiling(16)

#HQVGA (240x160 resolution) and grayscale are the best for face tracking
sensor.set_framesize(sensor.HQVGA)
sensor.set_pixformat(sensor.GRAYSCALE)

#load Haar cascade (already included by OpenMV IDE)
#higher stage is slower but more accurate. By default, use all stages
#"frontalface" model is provided by OpenMV. Customized model can also be supported.
face_cascade=image.HaarCascade("frontalface", stages=25)
print(face_cascade)

#FPS clock, Returns a clock object
clock = time.clock()

while (True):
#Starts tracking elapsed time
    clock.tick()

#Takes a picture using the camera and returns an image object.
    img=sensor.snapshot()

#find the face
#scale: lower scale value can detect smaller objects
#threshold: higher threshold gives faster detection, with more false
    objects=img.find_features(face_cascade, threshold=0.75, scale_factor=1.35)
#objects=img.find_features(face_cascade, threshold=0.5, scale=1.5)

#draw the found face with rectangle
    for r in objects:
        img.draw_rectangle(r)

#print FPS
    print(clock.fps())





