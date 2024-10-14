from machine import Pin, PWM, time_pulse_us
import time

# GY-53 Sensor Configuration (PWM Output)
PWM_PIN = Pin(6, Pin.IN)

# Function to read the distance of the GY-53 in PWM mode
def get_distance():
    pulse_width = time_pulse_us(PWM_PIN, 1)  # High pulse duration in µs
    if pulse_width < 0:
        return -1  # Sensor reading error
    return pulse_width/100  # Pulse width corresponds to distance in mm