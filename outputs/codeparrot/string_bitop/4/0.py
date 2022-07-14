from typing import List

def string_nor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOR on these inputs and return result also as a string.
    >>> string_nor('010', '110')
    '001'
    """
    if len(a) != len(b):
        return False
    if len(a) == 0:
        return True
    if len(b) == 0:
        return False
    return ''.join(a) == ''.join(b)


def string_nor_list(a: str, b: str) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOR on these inputs and return result also as a list.
    >>> string_nor_list('010', '110')
    ['001', '010', '110']
    """
    if len(a) != len(b):
        return False
    if len(a) == 0:
        return True
    if len(b) == 0:
        return False
    return [string_nor(a[i:i + 2], b[i:i + 2]) for i in range(0, len(a), 2)]


def string_nor_list_of_strings(a: str, b: str) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOR on these inputs and return result also as a list.
    >>> string_nor_list_of_strings('010', '110')
    ['001', '010', '110']
    """
    if len(a) != len(b):
        return False
    if len(a) == 0:
        return True
    if len(b) == 0:
        return False
    return [string_nor(a[i:i + 2], b[i:i + 2]) for i in range(0, len(a), 2)]


def string_nor_list_of_strings_of_lists(a: str, b: str) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOR on these inputs and return result also as a list.
    >>> string_nor_