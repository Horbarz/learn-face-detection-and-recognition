'''
Chapter 12: Face Detection and Recognition
'''

# Import the OpenCV library
import cv2
print ('hello')

# Initialize a face cascade using the frontal haar cascade provided
# with the OpenCV2 library. This will  be required for face detection 
# in an image.
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

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

