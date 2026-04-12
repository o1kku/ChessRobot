"""
A module to control electromagnet via a MOSFET switch.
"""
try:
    from gpiozero import OutputDevice
except ImportError:
    print("Warning: gpiozero not found. Electromagnet entering mock-mode.")
    class OutputDevice:
        def __init__(self, pin, initial_value=False):
            self.pin = pin
            self.active = initial_value
        def on(self): 
            self.active = True
            print(f"[MOCK] Electromagnet (Pin {self.pin}) turned ON")
        def off(self): 
            self.active = False
            print(f"[MOCK] Electromagnet (Pin {self.pin}) turned OFF")
        def toggle(self):
            self.active = not self.active
            state = "ON" if self.active else "OFF"
            print(f"[MOCK] Electromagnet (Pin {self.pin}) toggled to {state}")
        @property
        def is_active(self): return self.active

class Electromagnet:
    """
    A class to control a small electromagnet via a MOSFET switch.
    
    Attributes:
        pin (int): The GPIO pin number connected to the MOSFET Gate.
    """

    def __init__(self, pin, initial_value=False):
        """
        Initializes the electromagnet.
        
        :param pin: GPIO pin number (BCM).
        :param initial_value: Whether the magnet starts as ON or OFF.
        """
        # active_high=True means setting the pin to HIGH turns the MOSFET ON.
        self._magnet = OutputDevice(pin, initial_value=initial_value)

    def turn_on(self):
        """Activates the electromagnet."""
        self._magnet.on()

    def turn_off(self):
        """Deactivates the electromagnet."""
        self._magnet.off()

    @property
    def is_active(self):
        """Returns True if the electromagnet is currently powered."""
        return self._magnet.is_active

    def toggle(self):
        """Toggles the state of the electromagnet."""
        self._magnet.toggle()