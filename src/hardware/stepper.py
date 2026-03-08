"""
Module for controlling stepper motors via the ULN2003 driver.
"""

import time

try:
    from gpiozero import OutputDevice
except ImportError:
    print("Warning: gpiozero is not available. Entering mock-mode.")
    class OutputDevice:
        def __init__(self): self.pin = pin; self.value = 0
        def __repr__(self): return f"Pin({self.pin})"

class StepMotor:
    """
    A class to control a 28BYJ-48 stepper motor 
    using a ULN2003 driver.

    Attributes:
        pins (list): A list of GPIO pins (IN1, IN2, IN3, IN4).
        delay (float): The delay between steps in seconds.
    """

    # Half-step sequence for 28BYJ-48 motor.
    _STEP_SEQUENCE = [
        [1, 0, 0, 0], [1, 1, 0, 0],
        [0, 1, 0, 0], [0, 1, 1, 0],
        [0, 0, 1, 0], [0, 0, 1, 1],
        [0, 0, 0, 1], [1, 0, 0, 1]
    ]

    def __init__(self, pins, delay=0.002):
        """
        Initialize the stepper motor.
        """
        self.delay = delay
        self.pins = [OutputDevice(pin) for pin in pins]

    def _make_step(self, sequence):
        """
        Private method to make the motor do one step.

        Args:
            sequence (list): _STEP_SEQUENCE in correct order
        """
        for step in sequence:
            for pin, value in zip(self.pins, step):
                pin.value = value
                time.sleep(self.delay)
        
    def step(self, steps_nbr, direction=1):
        """
        Moves the motor by a pecified number of steps.
        
        Args:
            steps (int): The number of steps to move.
            direction (int): 1 for closer, -1 for further.
        """
        # Direction
        sequence = self._STEP_SEQUENCE if direction == 1 else self._STEP_SEQUENCE[::-1]

        # Make a step steps_nbr times in correct direction
        for _ in range(steps_nbr):
            self._make_step(sequence)