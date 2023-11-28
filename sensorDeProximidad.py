from machine import Pin
import utime

trigger = Pin(20, Pin.OUT)
echo = Pin(21, Pin.IN)

def measure_distance():
    trigger.low()
    utime.sleep_us(2)

    trigger.high()
    utime.sleep_us(5)
    trigger.low()
     
    #pulse_duration = time_pulse_us(echo, Pin.high)

    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us() 
  # Mide la duracion del echo pulse en microsegundos
    pulse_duration = signalon - signaloff
   
# Calcula la distancia en cm usando la velocidad del sonido (343 m/s)
    distance = (pulse_duration * 0.0343) / 2
    distance = "{:.2f}".format(distance)
    
    print(distance + " cm")
    return str(distance)    



