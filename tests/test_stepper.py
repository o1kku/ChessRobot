import pytest
from unittest.mock import patch
from src.hardware.stepper import StepMotor


@pytest.fixture
def motor():
    return StepMotor((1, 2, 3, 4))


# --- Initialisation ---

def test_init_creates_correct_number_of_pins(motor):
    assert len(motor.pins) == 4

def test_init_default_delay(motor):
    assert motor.delay_sec == 0.002

def test_init_custom_delay():
    motor = StepMotor((1, 2, 3, 4), delay_sec=0.005)
    assert motor.delay_sec == 0.005


# --- step() ---

def test_step_completes_and_clears_running_flag(motor):
    with patch("src.hardware.stepper.time.sleep"):
        motor.step(1)
    assert motor._running is False

def test_step_zero_steps_does_not_sleep(motor):
    with patch("src.hardware.stepper.time.sleep") as mock_sleep:
        motor.step(0)
    mock_sleep.assert_not_called()

def test_step_forward_and_backward_do_not_raise(motor):
    with patch("src.hardware.stepper.time.sleep"):
        motor.step(2, direction=1)
        motor.step(2, direction=-1)


# --- stop() ---

def test_stop_clears_running_flag(motor):
    motor._running = True
    motor.stop()
    assert motor._running is False

def test_stop_zeros_all_pins(motor):
    motor.stop()
    for pin in motor.pins:
        assert pin.value == 0
