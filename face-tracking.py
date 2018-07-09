'''
Chapter 12: Face Detection and Recognition
Tracking the Face

Aileen
July 9th, 2018
'''

import dilib 

# Create the tracker we will use to recognize face in different frames
# we get from the webcam
tracker = dlib.correlation_tracker()

# The Boolean variable we use to keep track whether we are
# using dlib tracker or not
trackingFace = 0

'''
# Within infinite loop...
 1. Determine whether the dlib correlation tracker is currently tracking
    a region in the image
 2. If NOT, use similar code from face-detection.py to find the largest face, but
    instead of drawing a rectangle, use the found coordinates to initialize the 
    correlation tracker
'''
