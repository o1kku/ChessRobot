import pytest
from unittest.mock import patch
from src.hardware.servo import ServoMotor


@pytest.fixture
def servo():
    return ServoMotor(pin=13)


# --- Initialisation ---

def test_init_creates_internal_servo(servo):
    assert servo.servo is not None

def test_init_custom_angles():
    s = ServoMotor(pin=13, min_angle=-45, max_angle=45, initial_angle=10)
    assert s.servo is not None


# --- set_angle() ---

def test_set_angle_assigns_to_servo(servo):
    with patch("src.hardware.servo.time.sleep"):
        servo.set_angle(45)
    assert servo.servo.angle == 45

def test_set_angle_sleeps_for_settle(servo):
    with patch("src.hardware.servo.time.sleep") as mock_sleep:
        servo.set_angle(45)
    mock_sleep.assert_called_once_with(ServoMotor._DELAY_SEC)


# --- go_to_min / go_to_max / center ---

def test_go_to_min_calls_servo_min(servo):
    with patch("src.hardware.servo.time.sleep"):
        servo.go_to_min()
    servo.servo.min.assert_called_once()

def test_go_to_max_calls_servo_max(servo):
    with patch("src.hardware.servo.time.sleep"):
        servo.go_to_max()
    servo.servo.max.assert_called_once()

def test_center_calls_servo_mid(servo):
    with patch("src.hardware.servo.time.sleep"):
        servo.center()
    servo.servo.mid.assert_called_once()


# --- current_angle property ---

def test_current_angle_returns_servo_angle(servo):
    servo.servo.angle = 30
    assert servo.current_angle == 30
