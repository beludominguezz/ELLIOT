#import os
#os.system("pip install roboflow")
import cv2
import requests
import numpy as np
from roboflow import Roboflow
from picamera2 import Picamera2
import time
from io import BytesIO
import soloFuncionesMotor

picam2 = Picamera2()
picam2.start()
time.sleep(1)
#ruta_imagenes = "/home/elliot/Pictures"

rf = Roboflow(api_key= "1khFRpWqEw456VNlfNNJ")
project = rf.workspace().project("elliot1")
model = project.version(2).model

with picam2 as camera:
    while True:
        #nombre_archivo = time.strftime("%Y%m%d%H%M%S") + ".jpg"
        #ruta_completa = ruta_imagenes + nombre_archivo
        
        camera.start_and_capture_file("test.jpg")
        
        prediction = model.predict("test.jpg", confidence=40, overlap=30)
        print(prediction.json())
        if len(prediction.json()["predictions"]) > 0:
            predicted_classes = prediction.json()["predictions"][0]["class"]
            #print("clase", predicted_classes)
            #if "Yellow-vest" in predicted_classes:
            soloFuncionesMotor.adelante()
            print("chaleco amarillos detectado. Avanzando")
                
            #else:
                #print("chaleco no detectado. Frenando")
        else:
            
            soloFuncionesMotor.freno()
            print("chaleco no detectado. Frenando")
            
        time.sleep(5)
