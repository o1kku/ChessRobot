"""
Module for controlling stepper motors via the ULN2003 driver.
"""

import time

try:
    from gpiozero import OutputDevice
except ImportError:
    print("Warning: gpiozero is not available. Stepper motor entering mock-mode.")
    class OutputDevice:
        def __init__(self, pin): self.pin = pin; self.value = 0
        def __repr__(self): return f"Pin({self.pin})"

class StepMotor:
    """
    A class to control a 28BYJ-48 stepper motor 
    using a ULN2003 driver.

    Attributes:
        pins (list): A list of GPIO pins (IN1, IN2, IN3, IN4).
        delay_sec (float): The delay between steps in seconds.
    """

    # Half-step sequence for 28BYJ-48 motor.
    _STEP_SEQUENCE = [
        [1, 0, 0, 0], [1, 1, 0, 0],
        [0, 1, 0, 0], [0, 1, 1, 0],
        [0, 0, 1, 0], [0, 0, 1, 1],
        [0, 0, 0, 1], [1, 0, 0, 1]
    ]

    def __init__(self, pins, delay_sec=0.002):
        """
        Initialize the stepper motor.

        :param pins: A list of GPIO pins (IN1, IN2, IN3, IN4).
        :param delay_sec: The delay between steps in seconds.
        """
        self.delay_sec = delay_sec
        self.pins = [OutputDevice(pin) for pin in pins]
        self.running = False

    def stop(self):
        """
        Stops the motor movement immediately and clears pins.
        """
        self._running = False
        for pin in self.pins:
            pin.value = 0

    def _make_step(self, sequence):
        """
        Make the motor do one full sequence cycle.

        :param sequence: _STEP_SEQUENCE in correct order
        """
        for step in sequence:
            # Check if stop() is called.
            if not self._running:
                return
            for pin, value in zip(self.pins, step):
                pin.value = value
                time.sleep(self.delay_sec)
        
    def step(self, steps_nbr, direction=1):
        """
        Moves the motor by a pecified number of steps.
        
        :param steps: The number of steps to move.
        :param direction: 1 for clockwise, -1 for counterclockwise.
        """
        self._running = True
        # Direction
        sequence = self._STEP_SEQUENCE if direction == 1 else self._STEP_SEQUENCE[::-1]

        # Make a step steps_nbr times in correct direction
        for _ in range(steps_nbr):
            if not self._running:
                break
            self._make_step(sequence)
        
        self._running = False