#Wallfollow modul
#main.py 
from machine import Pin, PWM, time_pulse_us
import time
from motor import motor_forward, motor_stop
from GY53 import get_distance
TARGET_DISTANCE = 10  # Target distance of 10 cm (100 mm)
TOLERANCE = 0.1  # Tolerance  +/- 1 cm (10 mm)
# Function to adjust the motors according to the distance from the wall
def wall_follow():
    while True:
        distance = get_distance()  # Read distance via PWM
        if distance == -1:
            print("Sensor reading error")
        else:
            print(f"Distance: {distance} cm")
            # If the vehicle is too close to the wall (less than 10 cm)
            if distance < TARGET_DISTANCE - TOLERANCE:
                # The vehicle turns slightly to the left (left engine faster)
                print("Too close to the wall, turn left")
                motor_forward(0.5, 0.2)  # Le moteur gauche avance plus vite que le droit
           # If the vehicle is far from the wall (more than 10 cm)
            elif distance > TARGET_DISTANCE + TOLERANCE:
                # The vehicle turns slightly to the right (right engine faster)
                print("Too far from the wall, turn right")
                motor_forward(0.2, 0.5)  # The right motor moves faster than the left
            # If the vehicle is in the correct distance from the wall (almost 10 cm)
            else:
                # The vehicle is moving straight ahead
                print("Correct distance, go straight ahead")
                motor_forward(0.4, 0.4)  # Both engines move at the same speed                
        time.sleep(1)  # Short pause to avoid a too fast loop
# Execution of the main program
wall_follow()



