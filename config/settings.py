"""
Global configuration settings for the robot hardware.
Contains GPIO pin mappings and default operational parameters.
"""

# Stepper Motors (ULN2003 uses 4 pins each)
STEPPER_HEIGHT_PINS = (7, 1, 11, 0)
STEPPER_DISTANCE_PINS = (5, 6, 19, 26)

# Servo Motor
SERVO_PIN = 13

# Limit Switches
SWITCH_ROTATE_PIN = 16
SWITCH_DISTANCE_PIN = 20
SWITCH_HEIGHT_PIN = 21

# Electromagnet
MAGNET_PIN = 12

# Operational Defaults
DEFAULT_STEP_DELAY = 0.002