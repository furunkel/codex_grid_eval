
from typing import List

def string_xand(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XAND on these inputs and return result also as a string.
    >>> string_xand('010', '110')
    '011'
    """
    return bin(int(a, 2) ^ int(b, 2))[2:]

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '010'
    """
    return bin(int(a, 2) ^ int(b, 2))[2:]

def string_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary AND on these inputs and return result also as a string.
    >>> string_and('010', '110')
    '100'
    """
    return bin(int(a, 2) & int(b, 2))[2:]

def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary OR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '111'
    """
    return bin(int(a, 2) | int(b, 2))[2:]

def string_not(a: str) -> str:
    """ Input is a string consisting of only 1s and 0s.
    Perform binary NOT on these inputs and return result also as a string.
    >>> string_not('010')
    '110'
    """
    return bin(int(a, 2) ^ 1)[2:]

def string_concat(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary concatenation on these inputs and return result also as a string.
    >>> string_concat('010', '110')
    '011'
    """
    return bin(int(a, 2) ^ int(b, 2))[2:]

def string_length(a: str) -> str:
    """ Input is a string consisting of only 1s and 0s.
    Perform binary length on these inputs and return result also as a string.
    >>> string_length('010')
    '11'
    """
    return bin(int(a, 2))[2:]

def string_substring(a: str, b: str, start: int, end: int) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary substring on these inputs and return result also as a string.
    >>> string_substring('010', '110', 2, 3)
    '110'
    """
    return bin(int(a, 2) ^ int(b, 2))[2:][start:end]

def string_concat_ws(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary concatenation on these inputs and return result also as a string.
    >>> 