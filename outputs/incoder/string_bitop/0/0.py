
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_int = 0
    b_int = 0
    for index, char in enumerate(b):
        if char == '1':
            a_int = a_int ^ 1
        else:
            b_int = b_int ^ 1
    return str(a_int ^ b_int)

def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010', '110'], ['100', '010'])
    ['100', '010']
    """
    a_int = 0
    b_int = 0
    for index, char in enumerate(b):
        if char == '1':
            a_int = a_int ^ 1
        else:
            b_int = b_int ^ 1
    return list(map(str, (a_int ^ b_int)))

def string_xor_list_2(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list_2(['010', '110'], ['100', '010'])
    ['100', '010']
    """
    a_int = 0
    b_int = 0
    for index, char in enumerate(b):
        if char == '1':
            a_int = a_int ^ 1
        else:
            b_int = b_int ^ 1
    return list(map(str, (a_int ^ b_int)))

def string_xor_list_3(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list_3(['010', '110'], ['100', '010'])
    ['100', '010']
    """
    a_int = 0
    b_int = 0
    for index, char in enumerate(b):
        if char == '1':
            a_int = a_int ^ 1
        else:
            b_int = b_int ^ 1
    return list(map(str, (a_int ^ b_int)))

def string_xor_list_4(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list_4(['010', '110'], ['100', '010'])
    ['100', '010']
    """
    a_int = 0
    b_int = 0
    for index, char in enumerate(b):
        if char == '1':
            a_int = a_int 