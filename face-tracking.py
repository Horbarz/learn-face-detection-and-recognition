'''
Chapter 12: Face Detection and Recognition
Tracking the Face

Aileen
July 9th, 2018
'''

# How to install dlib on Mac:
# https://www.learnopencv.com/install-dlib-on-macos/ :')
import dlib 
import cv2

# Display OpenCV Version :') Need at least 3.1.0
print ('OpenCV Version: ', cv2.__version__)

# --------------------------------------------------------------
# From face-detection.py...

HAARCASCADE_PATH = '../../../Downloads/opencv-3.4.2/data/haarcascades'

# Initialize a face cascade using the frontal haar cascade provided
# with the OpenCV2 library. This will  be required for face detection 
# in an image.
faceCascade = cv2.CascadeClassifier((HAARCASCADE_PATH + '/haarcascade_frontalface_default.xml'))

# The desired output widthand height, can be modified to the needs.
OUTPUT_SIZE_WIDTH = 700
OUTPUT_SIZE_HEIGHT = 600

# Open the first webcam device
capture = cv2.VideoCapture(0)

# Create two opencv named windows for showing the input, output images.
cv2.namedWindow('base-image', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('result-image', cv2.WINDOW_AUTOSIZE)

# Position the windows next to each other
cv2.moveWindow('base-image', 20, 200)
cv2.moveWindow('result-image', 640, 200)

# Start the window thread for the two windows we are using
cv2.startWindowThread()

rectangleColor = (0, 100, 255)

# --------------------------------------------------------------

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
while True:
    # --------------------------------------------------------------
    # From face-detection.py...

    if capture.isOpened() == False:
        print("Some error opening camera :'(")
        break

    # Retrieve the latest image from the webcam
    rc, fullSizeBaseImage = capture.read()

    # Resize the image to 520x420
    baseImage = cv2.resize(fullSizeBaseImage, (520, 420))

    # Check if a key was pressed and if it was Q or q, then destroy all
    # open cv windows and exit the application, stopping the infinite loop
    pressedKey = cv2.waitKey(2)
    if (pressedKey == ord('Q')) | (pressedKey == ord('q')):
        print('exit button pressed')
        break

    # --------------------------------------------------------------


    # If we are not tracking a face, then try to detect one using
    # the above code itself
    if not trackingFace:
        # We will be using a gray colored image for face detection.
        # So we need to convert the baseImage captured by webcam to a gray-based image
        gray = cv2.cvtColor(baseImage, cv2.COLOR_BGR2GRAY)
        # Now use the haar cascade detector to find all faces in the image
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)

        # In the console, we can show that we are using this method
        # for detecting a face for the first time
        print('Using the cascade detector to detect face')

        # --------------------------------------------------------------
        # From face-detection.py...
        # As we are only interested in the 'largest' face, we need to
        # calculate the largest area of the found rectangle.
        # For this, first initialize the required variables to 0.
        maxArea = 0
        x = 0
        y = 0
        w = 0
        h = 0

        # Loop over all faces found in the image and check if the area for this face
        # is the largest so far
        for(_x, _y, _w, _h) in faces:
            if _w * _h > maxArea:
                x = _x
                y = _y
                w = _w
                h = _h
            maxArea = w * h
        # --------------------------------------------------------------


        if maxArea > 0:
            # Initialize the tracker
            tracker.start_track(baseImage,
                dlib.rectangle(x-10, y-20, x+w+10, y+h+20))

            # Set the indicator variable such that we know the
            # tracker is tracking a face in the image
            trackingFace = 1

    # Check if the tracker is actively tracking a face in the image
    if trackingFace:
        
        # Update the tracker and request information about the
        # quality of the tracking update
        trackingQuality = tracker.update(baseImage)

        # If the tracking quality is good enough, determine the
        # updated position of the tracked region and draw the rectangle
        if trackingQuality >= 9.0:
            trackedPosition = tracker.get_position()

            t_x = int(trackedPosition.left())
            t_y = int(trackedPosition.top())
            t_w = int(trackedPosition.width())
            t_h = int(trackedPosition.height())
            cv2.rectangle(resultImage, (t_x, t_y),
                (t_x+t_w, t_y+t_h),
                rectangleColor, 2)
        
        else:
            # If the quality of the tracking update is not good enough
            # for us (e.g., the face being tracked moved out of the screen)
            # we stop the tracking of the face and in the next loop we will find 
            # the largest face in the image again
            trackingFace = 0

        

