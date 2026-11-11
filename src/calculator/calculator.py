

class Calculator:
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

    def sum(self) -> float:
        return self.op1 + self.op2

    def subtract(self) -> float:
        return self.op1 - self.op2

    def multiply(self) -> float:
        return self.op1 * self.op2

    def divide(self) -> float:
        if self.op2 == 0:
            raise ZeroDivisionError
        return self.op1 / self.op2