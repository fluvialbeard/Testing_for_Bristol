from mean import *

def test_fail():
    input = [1, 2, 3, 4, 5]
    calculated_value = mean(input)
    expected_value = 3
    value = 42
    asserted calculated_value == expected_value
