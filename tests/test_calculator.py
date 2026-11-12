"""Calculator test module"""

import pytest

from calculator.calculator import Calculator


class TestCalculator:
    @pytest.fixture
    def calculator(self):
        return Calculator(2, 2)

    @pytest.fixture
    def calculator_zero(self):
        return Calculator(2, 0)

    def test_add(self, calculator):
        assert calculator.sum() == 4

    def test_subtract(self, calculator):
        assert calculator.subtract() == 0

    def test_multiply(self, calculator):
        assert calculator.multiply() == 4

    def test_divide(self, calculator):
        assert calculator.divide() == 1

    def test_divide_zero(self, calculator_zero):
        with pytest.raises(ZeroDivisionError):
            assert calculator_zero.divide()

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (-1, -2, -3),
        (2.5, 3.5, 6.0),
    ])
    def test_add_parametrized(self, a, b, expected):
        calc = Calculator(a, b)
        assert calc.sum() == expected


