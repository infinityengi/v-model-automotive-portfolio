import pytest
from code.controller.controller import Controller


def test_zero_input():
    """
    Ensure controller returns approximately 0 for zero lateral error.
    """
    c = Controller()
    assert abs(c.compute_control(0.0)) < 1e-6
