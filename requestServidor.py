from picamera2 import Picamera2
import cv2
import time
import requests
import numpy as np
from io import BytesIO

picam2 = Picamera2()
picam2.start()
time.sleep(1)

cv2.namedWindow ('transmision en vivo', cv2.WINDOW_NORMAL)

#direccion del servidor(puede ser localhost: misma maquina, o )
server_url = "http://169.254.244.41:5000/detect"

try:
    while True:
        array = picam2.capture_array("main")
        #convertir imagen de BGR a RGB
        array_rgb = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
        
        #convertir la imagen a JPEG
        _, img_encoded = cv2.imencode('.jpg', array_rgb)
        img_bytes = img_encoded.tobytes()
        
        #para mandar la imagen al servidor
        response = requests.post(server_url, files={'image': ('image.jpg', BytesIO(img_bytes))})
       
       #recibir los resultados del servidor
        results = response.json()
        
        
       cv2.imshow('transmision en vivo', array_rgb)
       
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#finally:
    picam2.stop()
   # cv2.destroyAllWindows()
