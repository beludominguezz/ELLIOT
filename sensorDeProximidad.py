from machine import Pin
import utime

# Define the GPIO pin numbers for the trigger and echo pins
#ECHO_PIN = 20
#TRIGGER_PIN = 21

# Initialize trigger and echo pins
trigger = Pin(20, Pin.OUT)
echo = Pin(21, Pin.IN)

def measure_distance():
    # Ensure trigger is low initially
    trigger.low()
    utime.sleep_us(2)

    # Send a 10 microsecond pulse to the trigger pin
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
     
  # Measure the duration of the echo pulse (in microseconds)
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

    # Wait for 1 second before taking the next measurement
    



