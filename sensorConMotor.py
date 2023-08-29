from machine import Pin, time_pulse_us
from time import sleep_us, sleep

//sensor
ECHO_PIN = 20
TRIGGER_PIN = 21

trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

//motor
In1=Pin(3,Pin.OUT) 
In2=Pin(2,Pin.OUT)  
EN_A=Pin(4,Pin.OUT)


In3=Pin(1,Pin.OUT)  
In4=Pin(0,Pin.OUT)  
EN_B=Pin(5,Pin.OUT)


EN_A.high()
EN_B.high()

def adelante():
    In1.high()
    In2.low()
    In3.high()
    In4.low()
    
def atras():
    In1.low()
    In2.high()
    In3.low()
    In4.high()


def giro_der():
    In1.low()
    In2.low()
    In3.low()
    In4.high()
    
def giro_izq():
    In1.low()
    In2.high()
    In3.low()
    In4.low()


def freno():
    In1.low()
    In2.low()
    In3.low()
    In4.low()
    
def measure_distance():
    # el trigger va low al comienzo
    trigger.low()
    sleep_us(2)

    # Send a 10 microsecond pulse to the trigger pin
    trigger.high()
    sleep_us(10)
    trigger.low()

    # Measure the duration of the echo pulse (in microseconds)
    pulse_duration = time_pulse_us(echo, Pin.high)

    # Calculate the distance (in centimeters) using the speed of sound (343 m/s)
    distance = pulse_duration * 0.0343 / 2
    return distance

while True:
    if distance() == 1: 
            print("Objeto detectado, frenando motores")
            freno()
        else:
            print("Nada detectado, avanzando")
            adelante()

        utime.sleep(0.1)  

if __name__ == "__main__":
    main()