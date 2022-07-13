
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

def string_xor_list(a: str, b: List[str]) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return [string_xor(a, x) for x in b]

def string_xor_list_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return [string_xor(x, y) for x in a for y in b]

def string_xor_list_list_list(a: List[str], b: List[str], c: List[str]) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return [string_xor(x, y) for x in a for y in b for z in c]

def string_xor_list_list_list_list(a: List[str], b: List[str], c: List[str], d: List[str]) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return [string_xor(x, y) for x in a for y in b for z in c for w in d]

def string_xor_list_list_list_list_list(a: List[str