from typing import List

def string_nand(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NAND on these inputs and return result also as a string.
    >>> string_nand('010', '110')
    '101'
    """
    if len(a) != len(b):
        return False
    result = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            result += str(a[i])
            result += ' '
    return result

def string_nand_n(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NAND on these inputs and return result also as a string.
    >>> string_nand_n('010', '110')
    '101'
    """
    if len(a) != len(b):
        return False
    result = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            result += str(a[i])
            result += ' '
    return result

def string_nand_n_n(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NAND on these inputs and return result also as a string.
    >>> string_nand_n_n('010', '110')
    '101'
    """
    if len(a) != len(b):
        return False
    result = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            result += str(a[i])
            result += ' '
    return result

def string_nand_n_n_n(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NAND on these inputs and return result also as a string.
    >>> string_nand_n_n('010', '110')
    '101'
    """
    if len(a) != len(b):
        return False
    result = ''
    for i in range(len(a)):
        if a[i]