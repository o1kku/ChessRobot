"""
Global configuration settings for the robot hardware.
Contains GPIO pin mappings and default operational parameters.
"""

# Stepper Motors (ULN2003 uses 4 pins each)
STEPPER_HEIGHT_PINS = (6, 13, 19, 26)
STEPPER_DISTANCE_PINS = (12, 16, 20, 21)

# Servo Motor
SERVO_PIN = 18

# Limit Switches
SWITCH_X_PIN = 17
SWITCH_Y_PIN = 27
SWITCH_Z_PIN = 22

# Electromagnet
MAGNET_PIN = 23

# Operational Defaults
DEFAULT_STEP_DELAY = 0.002