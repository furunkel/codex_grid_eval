
from typing import List

def string_nor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOR on these inputs and return result also as a string.
    >>> string_nor('010', '110')
    '001'
    """
    return ''.join(['1' if a[i] == '0' and b[i] == '0' else '0' for i in range(len(a))])

def string_nand(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NAND on these inputs and return result also as a string.
    >>> string_nand('010', '110')
    '101'
    """
    return ''.join(['0' if a[i] == '1' and b[i] == '1' else '1' for i in range(len(a))])

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(['1' if a[i] != b[i] else '0' for i in range(len(a))])

def string_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary AND on these inputs and return result also as a string.
    >>> string_and('010', '110')
    '010'
    """
    return ''.join(['1' if a[i] == '1' and b[i] == '1' else '0' for i in range(len(a))])

def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary OR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '110'
    """
    return ''.join(['0' if a[i] == '0' and b[i] == '0' else '1' for i in range(len(a))])

def string_not(a: str) ->