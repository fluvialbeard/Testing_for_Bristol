import numpy as np
from sinc2d import *

def test_sinc2d_norm():
    calculated_value = sinc2d(2.0,2.0)
    expected_value = 0.25*np.sin(2.0)*np.sin(2.0)
    assert calculated_value == expected_value

def test_sinc2d_edgeX():
    y = 1
    calculated_value = sinc2d(0,y)
    expected_value = np.sin(y) / y
    assert calculated_value == expected_value

def test_sinc2d_edgeY():
    x = 1
    calculated_value = sinc2d(x,0)
    expected_value = np.sin(x) / x
    assert calculated_value == expected_value

def test_sinc2d_corner():
    x, y = 0, 0
    expected_value = 1
    calculated_value = sinc2d(x,y)
    assert calculated_value == expected_value

    
