from machine import Pin, PWM

# Configuring DC motors with the L298N driver
MOTOR_LEFT_IN1 = Pin(4, Pin.OUT)
MOTOR_LEFT_IN2 = Pin(5, Pin.OUT)
MOTOR_RIGHT_IN1 = Pin(2, Pin.OUT)
MOTOR_RIGHT_IN2 = Pin(3, Pin.OUT)

pwm_left = PWM(Pin(8))  # ENA (PWM) for left engine
pwm_right = PWM(Pin(7))  # ENB (PWM) for right engine
pwm_left.freq(1000)  # PWM frequency for left motor
pwm_right.freq(1000)  # PWM frequency for right motor


# Function to move straight ahead
def motor_forward(speed_left, speed_right):
    MOTOR_LEFT_IN1.high()
    MOTOR_LEFT_IN2.low()
    MOTOR_RIGHT_IN1.high()
    MOTOR_RIGHT_IN2.low()
    pwm_left.duty_u16(int(speed_left * 65535))  # Adjust left motor speed (0-100%)
    pwm_right.duty_u16(int(speed_right * 65535))  # Adjust right motor speed (0-100%)

# Function to stop the engines
def motor_stop():
    MOTOR_LEFT_IN1.low()
    MOTOR_LEFT_IN2.low()
    MOTOR_RIGHT_IN1.low()
    MOTOR_RIGHT_IN2.low()
    pwm_left.duty_u16(0)
    pwm_right.duty_u16(0)

