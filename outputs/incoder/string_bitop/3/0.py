
from typing import List

def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary OR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '110'
    """
    return bin(int(a, 2) + int(b, 2))[2:]

def string_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary AND on these inputs and return result also as a string.
    >>> string_and('010', '110')
    '100'
    """
    return bin(int(a, 2) + int(b, 2))[2:]

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '010'
    """
    return bin(int(a, 2) ^ int(b, 2))[2:]

def string_not(a: str) -> str:
    """ Input is a string consisting of only 1s and 0s.
    Perform binary NOT on these inputs and return result also as a string.
    >>> string_not('010')
    '110'
    """
    return bin(int(a, 2) ^ 1)[2:]

def string_concat(a: str, b: str) -> str:
    """ Input are two strings a and b consisting of only 1s and 0s.
    Perform binary concatenation on these inputs and return result also as a string.
    >>> string_concat('010', '110')
    '011'
    """
    return bin(int(a, 2) + int(b, 2))[2:]

def string_length(a: str) -> str:
    """ Input is a string consisting of only 1s and 0s.
    Perform binary length on these inputs and return result also as a string.
    >>> string_length('010')
    '11'
    """
    return bin(int(a, 2))[2:]

def string_substring(a: str, b: str, c: str) -> str:
    """ Input are three strings a and b consisting of only 1s and 0s.
    Perform binary substring on these inputs and return result also as a string.
    >>> string_substring('010', '110', '001')
    '011'
    """
    return bin(int(a, 2) + int(b, 2) + int(c, 2))[2:]

def string_substrings(a: str, b: str, c: str, d: str) -> str:
    """ Input are four strings a and b consisting of only 1s and 0s.
    Perform binary substrings on these inputs and return result also as a string.
    >>> string_substrings('010', '110', '001', '001')
    '011'
    """
    return bin(int(a, 2) + int(b, 2) + int(c, 2) + int(d, 2))[2:]

def string_substrings_count(a: str, b: str, c: str, d: str, e: str) -> str:
    """ Input are five strings a and b consisting of only 1s and 0s.
    Perform binary substrings count on 