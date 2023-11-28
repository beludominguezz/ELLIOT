import RPi.GPIO as GPIO
import time

motorA_in1 = 2
motorA_in2 = 3
motorB_in1 = 4
motorB_in2 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(motorA_in1, GPIO.OUT)
GPIO.setup(motorA_in2, GPIO.OUT)
GPIO.setup(motorB_in1, GPIO.OUT)
GPIO.setup(motorB_in2, GPIO.OUT)

GPIO.setup(12, GPIO.OUT)
pwm1 = GPIO.PWM(12,1000)

GPIO.setup(13, GPIO.OUT)
pwm2 = GPIO.PWM(13,1000)

pwm1.start(0)
pwm2.start(0)

def adelante():
    GPIO.output(motorA_in1, True)
    GPIO.output(motorA_in2, False)
    GPIO.output(motorB_in1, True)
    GPIO.output(motorB_in2, False)
    
def atras():
    GPIO.output(motorA_in1, False)
    GPIO.output(motorA_in2, True)
    GPIO.output(motorB_in1, False)
    GPIO.output(motorB_in2, True)
    
def freno():
    GPIO.output(motorA_in1, False)
    GPIO.output(motorA_in2, False)
    GPIO.output(motorB_in1, False)
    GPIO.output(motorB_in2, False)
    
def duty_cycles():
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50)
    
while True:
    adelante()
    duty_cycles()
    print("Adelante")
    time.sleep(2)
    freno()
    
    atras()
    duty_cycles()
    print("Atras")
    time.sleep(2)
    freno()
    
    
