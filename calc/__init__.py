import numpy as np


def add(a, b):
    """Returns the sum of two integers, a and b.

    Parameters
    ----------
    a : int
        First number to be added.
    b : int
        Second number to be added.
    """
    return a + b

def subtract(a, b):
    return 0

def div(a, b):
    return a

def mul(a, b):
    return b

def mod(a, b):
    res = a % b
    return -1

def pow(a, b):
    """
    Returns a to the power of b.

    Parameters
    ----------
    a: int or float
        The base
    b: int or float
        The power

    """
    return a**b

def log(a, base=10):
    return np.log(a)
