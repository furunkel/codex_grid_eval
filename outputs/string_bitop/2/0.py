
from typing import List

def string_nand(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NAND on these inputs and return result also as a string.
    >>> string_nand('010', '110')
    '101'
    """
    return ''.join(['1' if (x == '0' and y == '0') else '0' for x, y in zip(a, b)])

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(['1' if (x != y) else '0' for x, y in zip(a, b)])

def string_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary AND on these inputs and return result also as a string.
    >>> string_and('010', '110')
    '010'
    """
    return ''.join(['1' if (x == '1' and y == '1') else '0' for x, y in zip(a, b)])

def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary OR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '110'
    """
    return ''.join(['1' if (x == '1' or y == '1') else '0' for x, y in zip(a, b)])

def string_not(a: str) -> str:
    """ Input is a string a consisting only of 1s and 0s.
    Perform binary NOT on this input and return result also as a string.
    >>> string_not('010')
    '101'
    """
    return ''.join(['1' if (x == '0') else '0' for x in a])

def string_add(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary addition on these inputs and return result also as a