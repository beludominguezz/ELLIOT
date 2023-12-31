from machine import Pin, time_pulse_us
from time import sleep_us, sleep

ECHO_PIN = 20
TRIGGER_PIN = 21

trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

def measure_distance():
    # el trigger va low al comienzo
    trigger.low()
    sleep_us(2)
    trigger.high()
    sleep_us(10)
    trigger.low()
    pulse_duration = time_pulse_us(echo, Pin.high)
    distance = pulse_duration * 0.0343 / 2
    return distance

def main():
    while True:
        distance = measure_distance()
        print("Distance: {:.2f} cm".format(distance))
                sleep(1)

if __name__ == "__main__":
    main()
