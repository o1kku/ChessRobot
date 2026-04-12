"""
Module for controlling a servo motor using PWM.
Includes a mock-mode for testing without hardware.
"""

import time

try:
    from gpiozero import AngularServo
except ImportError:
    print("Warning: gpiozero not found. ServoMotor entering mock-mode.")
    
    class AngularServo:
        """Mock version of gpiozero's AngularServo."""
        def __init__(self, pin, min_angle=-90, max_angle=90, initial_angle=0):
            self.pin = pin
            self.min_angle = min_angle
            self.max_angle = max_angle
            self._angle = initial_angle

        @property
        def angle(self):
            return self._angle

        @angle.setter
        def angle(self, value):
            if value is not None:
                # Clamp the angle to physical limits like the real library does
                if value < self.min_angle:
                    value = self.min_angle
                elif value > self.max_angle:
                    value = self.max_angle
            self._angle = value
            print(f"[MOCK] Servo (Pin {self.pin}) moved to angle: {self._angle}°")

        def min(self):
            self.angle = self.min_angle

        def max(self):
            self.angle = self.max_angle

        def mid(self):
            self.angle = (self.max_angle + self.min_angle) / 2

class ServoMotor:
    """
    A class to control a standard servo motor.

    Attributes:
        pin (int): The GPIO pin number (BCM).
        min_angle (int/float): The minimum angle the servo can reach.
        max_angle (int/float): The maximum angle the servo can reach.
    """
    # Delay in seconds for the servo to physically reach it's
    # position before the program moves on.
    _DELAY_SEC = 0.3

    def __init__(self, pin, min_angle=-90, max_angle=90, initial_angle=0):
        """
        Initializes the servo motor.

        :param pin: The GPIO pin connected to the servo's signal wire.
        :param min_angle: The minimum physical angle (usually -90).
        :param max_angle: The maximum physical angle (usually 90).
        :param initial_angle: The starting angle.
        """
        self.servo = AngularServo(
            pin, 
            min_angle=min_angle, 
            max_angle=max_angle, 
            initial_angle=initial_angle
        )

    def set_angle(self, angle):
        """
        Moves the servo to a specific angle.

        :param angle: The target angle in degrees.
        """
        self.servo.angle = angle
        
        time.sleep(self._DELAY_SEC) 

    def go_to_min(self):
        """Moves the servo to its minimum angle."""
        self.servo.min()
        time.sleep(self._DELAY_SEC)

    def go_to_max(self):
        """Moves the servo to its maximum angle."""
        self.servo.max()
        time.sleep(self._DELAY_SEC)

    def center(self):
        """Moves the servo to its center position (middle angle)."""
        self.servo.mid()
        time.sleep(self._DELAY_SEC)

    @property
    def current_angle(self):
        """Returns the current angle of the servo."""
        return self.servo.angle