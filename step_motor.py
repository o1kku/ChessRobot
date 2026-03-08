"""
step_motor.py

This file defines a class for operates a stepper motor.

Author: Oliver Ekman
"""


class StepMotor:
    """
    Class for controlling a stepper motor.
    """
    def __init__(self, pins):
        self.IN1 = OutputDevice(pins[0])
        self.IN2 = OutputDevice(pins[1])
        self.IN3 = OutputDevice(pins[2])
        self.IN4 = OutputDevice(pins[3])
    
