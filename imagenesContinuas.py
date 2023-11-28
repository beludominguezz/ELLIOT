from picamera2 import Picamera2
import cv2
import time

picam2 = Picamera2()
picam2.start()
time.sleep(1)

cv2.namedWindow ('transmision en vivo', cv2.WINDOW_NORMAL)

try:
    while True:
        array = picam2.capture_array("main")
        
        array_rgb = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
        
        cv2.imshow('transmision en vivo', array_rgb)
        
        time.sleep(3)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    picam2.stop()
    cv2.destroyAllWindows()