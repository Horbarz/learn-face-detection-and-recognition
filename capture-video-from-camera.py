import numpy as np 
import cv2 

cap = cv2.VideoCapture(0) # If cap does not initialize the capture, an error 
                          # will be shown

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read() # returns a bool - if frame is read correctly
                            # it returns True. otherwise, False

    # I can set the size of the window
    ret = cap.set(3, 320) # 3 is width property
    ret = cap.set(4, 240) # 4 is height propertly
                          # (See notes on cap.get(PropID) below)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Note: cap.get(propId) method returns different properties of the video (0 through 18)
# print(cap.get(0), '\n', cap.get(1))
# cap.get(3) and cap.get(4) =>  frame width and heigth


# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()