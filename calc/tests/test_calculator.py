from calc import calculator
import pytest

def test_add():
    result = calculator.add(3, 4)
    assert result == 7

def test_add_string():
    with pytest.raises(TypeError):
        calculator.add("string", 4)