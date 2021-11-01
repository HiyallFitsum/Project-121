import cv2
import numpy as np

cap = cv2.VideoCapture(0)

for i in range(60):
    ret, bg  = cap.read()

bg = np.flip(bg, axis = 1)

while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break

    img = np.flip(img, axis = 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

frame = cv2.resize(bg, (640, 480))
image = cv2.resize(img, (640, 480))

u_black = np.array([153, 70])
l_black = np.array([30, 30, 0])

mask = cv2.inRange(frame, l_black, u_black)
res = cv2.bitwise_and(frame, frame, mask = mask)

f = frame - res 
f = np.where(f == 0, image, f)


cap.release()
out.release()
cv2.destroyAllWindows()