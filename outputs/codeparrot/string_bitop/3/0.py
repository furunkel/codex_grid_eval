from typing import List

def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary OR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '110'
    """
    if a == b:
        return a
    else:
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(a, b))

def string_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary AND on these inputs and return result also as a string.
    >>> string_and('010', '110')
    '110'
    """
    if a == b:
        return a
    else:
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(a, b))

def string_not(a: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOT on these inputs and return result also as a string.
    >>> string_not('010', '110')
    '110'
    """
    if a == b:
        return a
    else:
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(a, b))

def string_not_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOT AND on these inputs and return result also as a string.
    >>> string_not_and('010', '110')
    '110'
    """
    if a == b:
        return a
    else:
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(a, b))

def string_not_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOT OR on these inputs and return result also as a string.
    >>> string_not_or('010', '110')
    '110'
    """
    if a == b: