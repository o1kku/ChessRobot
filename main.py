"""
This program provides a main interface for
controlling the ChessRobot on Raspberry Pi 5. 
"""

import time

from config.settings import STEPPER_DISTANCE_PINS
from src.hardware.stepper import StepMotor

def main():
    dist_motor = StepMotor(STEPPER_DISTANCE_PINS)

    dist_motor.step(500)
    time.delay(1)
    dist_motor.step(500, -1)

if __name__=="__main__":
    main()
