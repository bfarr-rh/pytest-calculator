from calc import calculator
import pytest

def test_add():
    result = calculator.add(3, 4)
    assert result == 7