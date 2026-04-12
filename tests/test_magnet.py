import pytest
from src.hardware.magnet import Electromagnet


@pytest.fixture
def magnet():
    return Electromagnet(pin=12)


# --- Initialisation ---

def test_init_creates_internal_output_device(magnet):
    assert magnet._magnet is not None

def test_init_default_is_off(magnet):
    # OutputDevice constructed with initial_value=False by default
    from unittest.mock import call
    import src.hardware.magnet as magnet_module
    magnet_module.OutputDevice.assert_called_with(12, initial_value=False)

def test_init_can_start_on():
    m = Electromagnet(pin=12, initial_value=True)
    assert m._magnet is not None


# --- turn_on / turn_off / toggle ---

def test_turn_on_calls_on(magnet):
    magnet.turn_on()
    magnet._magnet.on.assert_called_once()

def test_turn_off_calls_off(magnet):
    magnet.turn_off()
    magnet._magnet.off.assert_called_once()

def test_toggle_calls_toggle(magnet):
    magnet.toggle()
    magnet._magnet.toggle.assert_called_once()


# --- is_active property ---

def test_is_active_reflects_device_state_true(magnet):
    magnet._magnet.is_active = True
    assert magnet.is_active is True

def test_is_active_reflects_device_state_false(magnet):
    magnet._magnet.is_active = False
    assert magnet.is_active is False
