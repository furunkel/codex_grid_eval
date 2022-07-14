from typing import List

def string_xnor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XNOR on these inputs and return result also as a string.
    >>> string_xnor('010', '110')
    '011'
    """
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b))

def string_xnor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XNOR on these inputs and return result also as a string.
    >>> string_xnor('010', '110')
    '011'
    """
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b))

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '011'
    """
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b))

def string_not(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOT on these inputs and return result also as a string.
    >>> string_not('010', '110')
    '011'
    """
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b))

def string_not_xnor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOT on these inputs and return result also as a string.
    >>> string_not_xnor('010', '110')
    '011'
    """
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b))

def string_not_xor