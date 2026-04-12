"""
Global configuration settings for the robot hardware.
Contains GPIO pin mappings and default operational parameters.
"""

# Stepper Motors — ULN2003 driver, pins map to IN1, IN2, IN3, IN4
STEPPER_HEIGHT_PINS = (7, 1, 11, 0)      # IN1–IN4 on height-axis ULN2003
STEPPER_DISTANCE_PINS = (5, 6, 19, 26)   # IN1–IN4 on distance-axis ULN2003

# Servo Motor — signal wire (PWM)
SERVO_PIN = 13

# Limit Switches — one per axis (KW12-3, normally open, pull-up enabled)
SWITCH_ROTATE_PIN = 16    # Rotation axis home position
SWITCH_DISTANCE_PIN = 20  # Distance axis home position
SWITCH_HEIGHT_PIN = 21    # Height axis home position

# Electromagnet — MOSFET gate (HIGH = magnet on)
MAGNET_PIN = 12

# Operational Defaults
DEFAULT_STEP_DELAY = 0.002