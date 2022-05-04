
from typing import List

def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary OR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '110'
    """
    return ''.join(str(int(a[i]) | int(b[i])) for i in range(len(a)))

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))

def string_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary AND on these inputs and return result also as a string.
    >>> string_and('010', '110')
    '010'
    """
    return ''.join(str(int(a[i]) & int(b[i])) for i in range(len(a)))

def string_not(a: str) -> str:
    """ Input is a string a consisting only of 1s and 0s.
    Perform binary NOT on this input and return result also as a string.
    >>> string_not('010')
    '101'
    """
    return ''.join(str(int(not int(a[i]))) for i in range(len(a)))

def string_shift_left(a: str, n: int) -> str:
    """ Input is a string a consisting only of 1s and 0s.
    Perform binary shift left on this input and return result also as a string.
    >>> string_shift_left('010', 1)
    '100'
    """
    return ''.join(str(int(a[i])) for i in range(n, len(a))) + ''.join(str(0) for i in range(n))

def string_shift_right(a: str, n: int) -> str:
    """ Input is a string a consisting only of 1s and 0s.
    Perform binary shift right on this input and return result also as a string.
    >>>