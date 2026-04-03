"""
A module for reading the state of a KW12-3 limit switch.
"""

try:
    from gpiozero import Button
except ImportError:
    print("Warning: gpiozero is not available. Entering mock-mode.")
    class Button:
        def __init__(self): self.pin = pin; self.value = 0
        def __repr__(self): return f"Pin({self.pin})"


class LimitSwitch:
    """
    A module for reading the state of a KW12-3 limit switch.
    """
    
    def __init__(self, pin, bounce_time=0.05):
        """
        Initializes the limit switch.
        
        :param pin: The GPIO pin number.
        :param bounce_time_sec: Time in seconds for software debouncing.
        """
        # pull_up=True enables the Raspberry Pi's internal pull-up resistor.
        self.switch = Button(pin, pull_up=True, bounce_time=bounce_time)

    @property
    def is_pressed(self):
        """Returns True if the switch is currently being pressed."""
        return self.switch.is_pressed

    def set_pressed_callback(self, callback_function):
        """
        Sets a function to be executed IMMEDIATELY when the switch 
        is pressed.

        :param callback_function: The function to be executed.
        """
        self.switch.when_pressed = callback_function

    def set_released_callback(self, callback_function):
        """
        Sets a function to be executed when the switch is released.

        :param callback_function: The function to be executed.
        """
        self.switch.when_released = callback_function