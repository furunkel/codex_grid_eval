
from typing import List

def string_xnor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XNOR on these inputs and return result also as a string.
    >>> string_xnor('010', '110')
    '011'
    """
    return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(a, b)])

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '010'
    """
    return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(a, b)])

def string_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary AND on these inputs and return result also as a string.
    >>> string_and('010', '110')
    '100'
    """
    return ''.join([chr(ord(a) & ord(b)) for a, b in zip(a, b)])

def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary OR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '011'
    """
    return ''.join([chr(ord(a) | ord(b)) for a, b in zip(a, b)])

def string_not(a: str) -> str:
    """ Input is a string consisting of only 1s and 0s.
    Perform binary NOT on these inputs and return result also as a string.
    >>> string_not('010')
    '110'
    """
    return ''.join([chr(ord(a) ^ 1) for a in a])

def string_concat(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary concatenation on these inputs and return result also as a string.
    >>> string_concat('010', '110')
    '01110'
    """
    return ''.join([chr(ord(a) + ord(b)) for a, b in zip(a, b)])

def string_split(a: str, b: str, delimiter: str = ' ') -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary concatenation on these inputs and return result also as a string.
    >>> string_split('010', '110', delimiter = '')
    '010'
    """
    return ''.join([chr(ord(a) + ord(b)) for a, b in zip(a, b)])

def string_split_reverse(a: str, b: str, delimiter: str = ' ') -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary concatenation on these inputs and return result also as a string.
    >>> string_split_reverse('110', '010', delimiter = '')
    '110'
    """
    return ''