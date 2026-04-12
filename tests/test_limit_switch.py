import pytest
from src.hardware.limit_switch import LimitSwitch


@pytest.fixture
def switch():
    return LimitSwitch(pin=16)


# --- Initialisation ---

def test_init_creates_internal_button(switch):
    assert switch.switch is not None

def test_init_custom_bounce_time():
    s = LimitSwitch(pin=16, bounce_time=0.1)
    assert s.switch is not None


# --- is_pressed property ---

def test_is_pressed_reflects_button_state_false(switch):
    switch.switch.is_pressed = False
    assert switch.is_pressed is False

def test_is_pressed_reflects_button_state_true(switch):
    switch.switch.is_pressed = True
    assert switch.is_pressed is True


# --- callbacks ---

def test_set_pressed_callback_assigns_to_when_pressed(switch):
    cb = lambda: None
    switch.set_pressed_callback(cb)
    assert switch.switch.when_pressed == cb

def test_set_released_callback_assigns_to_when_released(switch):
    cb = lambda: None
    switch.set_released_callback(cb)
    assert switch.switch.when_released == cb

def test_pressed_callback_is_callable(switch):
    called = []
    switch.set_pressed_callback(lambda: called.append(1))
    switch.switch.when_pressed()
    assert called == [1]
