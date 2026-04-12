"""
Mocks gpiozero at the sys.modules level before any hardware module is
imported. This causes every `from gpiozero import X` in src/hardware/ to
succeed and return a MagicMock, so tests run on any platform without GPIO
hardware present.
"""

import sys
from unittest.mock import MagicMock

sys.modules["gpiozero"] = MagicMock()
