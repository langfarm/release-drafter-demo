"""Example module of the fancy library, consuming the base library"""

from langfarm_core import adder2


def add3(x: int, y: int, z: int) -> int:
    """
    Adds three integers

    Args:
        x: the left operand
        y: the middle operand
        z: the right operand
    Returns:
        The sum of x, y, and z
    """
    return adder2.add2(adder2.add2(x, y), z)
