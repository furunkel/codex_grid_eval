from typing import List

def string_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary AND on these inputs and return result also as a string.
    >>> string_and('010', '110')
    '010'
    """
    if len(a) != len(b):
        raise ValueError("String and number of inputs must be equal")
    return ''.join(a) + ''.join(b)

def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary OR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '010'
    """
    if len(a) != len(b):
        raise ValueError("String or number of inputs must be equal")
    return ''.join(a) + ''.join(b)

def string_not(a: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOT on these inputs and return result also as a string.
    >>> string_not('010', '110')
    '010'
    """
    if len(a) != len(b):
        raise ValueError("String not of inputs must be equal")
    return ''.join(a)

def string_not_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOT OR on these inputs and return result also as a string.
    >>> string_not_or('010', '110')
    '010'
    """
    if len(a) != len(b):
        raise ValueError("String not of inputs must be equal")
    return ''.join(a) + ''.join(b)

def string_not_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOT AND on these inputs and return result also as a string.
    >>> string_not_and('010', '110')
    '010'
    """
    if len(a) != len(b):
        raise ValueError("String not of inputs must be equal