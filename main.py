"""
This program provides a main interface for
controlling the ChessRobot on Raspberry Pi 5. 

This is an init version for testing the
motors. The code below is an example code made by 
Krishna in June 15, 2024 and can be found from:
https://steppermotor.net/control-stepper-motor-with-raspberry-pi/#Raspberry_Pi_Python_and_a_TB6600_Stepper_Motor_Driver
"""

from gpiozero import OutputDevice
from time import sleep

# Define GPIO pins
IN1 = OutputDevice(29)
IN2 = OutputDevice(31)
IN3 = OutputDevice(35)
IN4 = OutputDevice(37)

# Define step sequence for half step
# To make it a one step, comment out lines with two ones
step_seq = [
    #[1, 0, 0, 1],
    [1, 0, 0, 0],
    #[1, 1, 0, 0],
    [0, 1, 0, 0],
    #[0, 1, 1, 0],
    [0, 0, 1, 0],
    #[0, 0, 1, 1],
    [0, 0, 0, 1]
]

def set_step(w1, w2, w3, w4):
    IN1.value = w1
    IN2.value = w2
    IN3.value = w3
    IN4.value = w4

def stepper_step(delay, steps):
    for _ in range(steps):
        for step in step_seq:
            set_step(step[0], step[1], step[2], step[3])
            sleep(delay)

try:
    while True:
        stepper_step(0.001, 512)  # Rotate forward
        sleep(1)
        #stepper_step(0.001, -512) # Rotate backward
        sleep(1)
except KeyboardInterrupt:
    pass