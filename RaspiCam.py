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
