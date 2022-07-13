
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 3 bit positions.
    """
    return bin(a ^ b).count('1') == 3


def find_diff_3(a, b):
    """
    Returns the bit position where the two numbers differ at exactly 3 bit positions.
    """
    return [i for i in range(len(a)) if a[i] != b[i]][0]


def find_diff_1(a, b):
    """
    Returns the bit position where the two numbers differ at exactly 1 bit positions.
    """
    return [i for i in range(len(a)) if a[i] != b[i]][0]


def find_diff_1_2(a, b):
    """
    Returns the bit position where the two numbers differ at exactly 1 bit positions.
    """
    return [i for i in range(len(a)) if a[i] != b[i]][1]


def find_diff_1_3(a, b):
    """
    Returns the bit position where the two numbers differ at exactly 1 bit positions.
    """
    return [i for i in range(len(a)) if a[i] != b[i]][2]


def find_diff_1_4(a, b):
    """
    Returns the bit position where the two numbers differ at exactly 1 bit positions.
    """
    return [i for i in range(len(a)) if a[i] != b[i]][3]


def find_diff_1_5(a, b):
    """
    Returns the bit position where the two numbers differ at exactly 1 bit positions.
    """
    return [i for i in range(len(a)) if a[i] != b[i]][4]


def find_diff_1_6(a, b):
    """
    Returns the bit position where the two numbers differ at exactly 1 bit positions.
    """
    return [i for i in range(len(a)) if a[i] != b[i]][5]


def find_diff_1_7(a, b):
    """
    Returns the bit position where the two numbers differ at exactly 1 bit positions.
    """
    return [i for i in