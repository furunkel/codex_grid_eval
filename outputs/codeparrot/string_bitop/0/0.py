from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b))

def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '100'
    """
    return ''.join(chr(ord(x) | ord(y)) for (x, y) in zip(a, b))

def string_not(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_not('010', '110')
    '100'
    """
    return ''.join(chr(ord(x) & ord(y)) for (x, y) in zip(a, b))

def string_shift(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_shift('010', '110')
    '100'
    """
    return ''.join(chr(ord(x) << 1) for (x, y) in zip(a, b))

def string_lshift(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_lshift('010', '110')
    '100'
    """
    return ''.join(chr(ord(x) << 1) for (x, y) in zip(a, b))

def string_rshift(a: str, b: str) -> str:
   