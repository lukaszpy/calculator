"""Calculator module - basic arithmetic operations."""


class Calculator:
    """Provides basic arithmetic operations."""

    def __init__(self, op1: float, op2: float):
        """Initialize calculator with two operands."""
        self.op1 = op1
        self.op2 = op2

    def sum(self) -> float:
        """Return sum of operands."""
        return self.op1 + self.op2

    def subtract(self) -> float:
        """Return difference between operands."""
        return self.op1 - self.op2

    def multiply(self) -> float:
        """Return product of operands."""
        return self.op1 * self.op2

    def divide(self) -> float:
        """Divide first operand by the second."""
        if self.op2 == 0:
            raise ZeroDivisionError("Divide by zero")

        return self.op1 / self.op2
