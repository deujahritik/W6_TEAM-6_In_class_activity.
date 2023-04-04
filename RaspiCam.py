import cv2
import time

# initialize the camera
camera = cv2.VideoCapture(0)
time.sleep(2)  # let the camera warm up

# capture an image
ret, frame = camera.read()

# save the image
cv2.imwrite("image.jpg", frame)

# release the camera
camera.release()



This code uses the OpenCV library to capture an image from the Raspberry Pi camera module connected to the Raspberry Pi.
The cv2.VideoCapture(0) function initializes the camera with ID 0, which corresponds to the first connected camera.
The time.sleep(2) function is used to allow the camera to warm up before capturing an image.

The camera.read() function captures a single frame from the camera and
returns a tuple containing a boolean value indicating whether the frame was successfully captured (True if successful, False otherwise) and the captured frame itself.

The cv2.imwrite("image.jpg", frame) function saves the captured frame as an image with the filename "image.jpg" in the current directory.

Finally, the camera.release() function is called to release the camera and free up system resources.

This code can be extended to capture multiple images and
perform additional image processing tasks such as object detection and analysis for smart plant care, as described in the scenario above.
