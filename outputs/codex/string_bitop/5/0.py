
from typing import List

def string_xnor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XNOR on these inputs and return result also as a string.
    >>> string_xnor('010', '110')
    '011'
    """
    return string_xor(string_not(string_xor(a, b)), '1')

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

def string_not(a: str) -> str:
    """ Input is a string a consisting only of 1s and 0s.
    Perform binary NOT on this input and return result also as a string.
    >>> string_not('010')
    '101'
    """
    return ''.join(str(int(x) ^ 1) for x in a)

def string_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary AND on these inputs and return result also as a string.
    >>> string_and('010', '110')
    '010'
    """
    return ''.join(str(int(x) & int(y)) for x, y in zip(a, b))

def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary OR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '110'
    """
    return ''.join(str(int(x) | int(y)) for x, y in zip(a, b))

def string_nand(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NAND on these inputs and return result also as a string.
    >>> string_nand('010', '110')
    '101'
    """
    return string_not(string_and(a, b))

def