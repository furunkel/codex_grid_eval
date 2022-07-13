
from typing import List

def string_nand(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NAND on these inputs and return result also as a string.
    >>> string_nand('010', '110')
    '101'
    """
    return bin(int(a, 2) & int(b, 2))[2:]

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '011'
    """
    return bin(int(a, 2) ^ int(b, 2))[2:]

def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary OR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '111'
    """
    return bin(int(a, 2) | int(b, 2))[2:]

def string_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary AND on these inputs and return result also as a string.
    >>> string_and('010', '110')
    '010'
    """
    return bin(int(a, 2) & int(b, 2))[2:]

def string_not(a: str) -> str:
    """ Input is a string consisting of 1s and 0s.
    Perform binary NOT on these inputs and return result also as a string.
    >>> string_not('010')
    '100'
    """
    return bin(int(not int(a), 2))[2:]

def string_concat(a: str, b: str) -> str:
    """ Input are two strings a and b consisting of 1s and 0s.
    Perform binary concatenation on these inputs and return result also as a string.
    >>> string_concat('010', '110')
    '011'
    """
    return bin(int(a, 2) | int(b, 2))[2:]

def string_contains(a: str, b: str) -> bool:
    """ Input are two strings a and b consisting of 1s and 0s.
    Perform binary containment on these inputs and return result also as a boolean.
    >>> string_contains('010', '110')
    True
    """
    return int(a, 2) & int(b, 2) > 0

def string_length(a: str) -> str:
    """ Input is a string consisting of 1s and 0s.
    Perform binary length on these inputs and return result also as a string.
    >>> string_length('010')
    '1'
    """
    return bin(int(a, 2))[2:]

def string_substring(a: str, b: str, start: int, end: int) -> str:
    """ Input are two strings a and b consisting of 1s and 0s.
    Perform binary substring on these inputs and return result also as a string.
    >>> string_substring('010', '110', 0, 1)
    '01'
    """
    return bin