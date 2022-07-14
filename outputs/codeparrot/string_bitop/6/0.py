from typing import List

def string_xand(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XAND on these inputs and return result also as a string.
    >>> string_xand('010', '110')
    '011'
    """
    return ''.join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '011'
    """
    return ''.join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

def string_not(a: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOT on these inputs and return result also as a string.
    >>> string_not('010')
    '011'
    """
    return ''.join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

def string_not_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOT on these inputs and return result also as a string.
    >>> string_not_xor('010', '110')
    '011'
    """
    return ''.join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

def string_not_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOT on these inputs and return result also as a string.
    >>> string_not_or('010', '110')
    '011'
    """
    return ''.join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

def string_not_xor_or(a: str, b: str