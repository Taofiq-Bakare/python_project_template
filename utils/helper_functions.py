"""
This file contains the helper functions used for the cli tool
"""
import numpy as np


def add_x(x: float, y: float) -> float:
    """
    A trivial implementation of the add function.

    Args:
        x (float): the first value to add
        y (float): the second value to add

    Raises:
        ValueError: Raises error if the value is not float

    Returns:
        float: floating point value.
    """
    try:
        res = np.float32(x) + np.float32(y)
    except ValueError:
        raise ValueError("Please provide float/int")
    return res
