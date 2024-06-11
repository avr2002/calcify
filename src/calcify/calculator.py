"""Calculator module."""


def add(a: float, b: float, *args: float) -> float:
    """Return the sum of all provided numbers. At least two numbers must be provided."""
    return a + b + sum(args)

def subtract(a: float, b: float) -> float:
    """Return the difference between a and b."""
    return a - b

def multiply(a: float, b: float, *args) -> float:
    """Return the product of all provided numbers. At least two numbers must be provided."""
    product = a * b
    for num in args:
        product *= num
    return product

def divide(a: float, b: float) -> float:
    """Return the division of a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
