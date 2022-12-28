# This file contains the helper functions used for the cli tool
import numpy as np


def add_x(x: float, y: float) -> float:
    try:
        res = np.float32(x) + np.float32(y)
    except ValueError:
        raise ValueError("Please provide float/int")
    return res
