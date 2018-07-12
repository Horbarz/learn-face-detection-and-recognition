'''
Chapter 12: Face Detection and Recognition
Face Recognition

Aileen
July 12th, 2018

"...identifies the name of person present in the video frame by matching the face
in each frame of video with the trained images and returns (and writes in a CSV file) the
label if the face in the frame is successfully matched..."
'''

# Import required libraries
import os
import re
import warnings
import scipy.misc
import cv2
import face_recognition # simple library built using dlib's face recognition
from PIL import Image
import argparse         # python library allowing you to add args to a file
import csv
# import os ??

