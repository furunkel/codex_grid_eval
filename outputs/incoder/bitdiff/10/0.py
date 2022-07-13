
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly five bit positions.
    """
    if a == b:
        return False
    bit_count = (a ^ b) >> 3
    if bit_count <= 5:
        return True
    else:
        return False


def bit_diff2(a, b):
    """
    Returns whether the two numbers differ at exactly two bit positions.
    """
    if a == b:
        return False
    bit_count = (a ^ b) >> 1
    if bit_count <= 2:
        return True
    else:
        return False


def bit_diff3(a, b):
    """
    Returns whether the two numbers differ at exactly three bit positions.
    """
    if a == b:
        return False
    bit_count = (a ^ b) >> 2
    if bit_count <= 3:
        return True
    else:
        return False


def bit_diff4(a, b):
    """
    Returns whether the two numbers differ at exactly four bit positions.
    """
    if a == b:
        return False
    bit_count = (a ^ b) >> 3
    if bit_count <= 4:
        return True
    else:
        return False


def bit_diff5(a, b):
    """
    Returns whether the two numbers differ at exactly five bit positions.
    """
    if a == b:
        return False
    bit_count = (a ^ b) >> 4
    if bit_count <= 5:
        return True
    else:
        return False


def bit_diff6(a, b):
    """
    Returns whether the two numbers differ at exactly six bit positions.
    """
    if a == b:
        return False
    bit_count = (a ^ b) >> 5
    if bit_count <= 6:
        return True
    else:
        return False


def bit_diff7(a, b):
    """
    Returns whether the two numbers differ at exactly seven bit positions.
    """
    if a == b:
        return False
    bit_count = (a ^ b) >> 6
    if bit_count <= 7:
        return True
    else:
        return False


def bit_diff8(a, b):
    """
    Returns whether the two numbers differ at exactly eight bit positions.
    """
    if a == b:
        return False
    bit_count = (a ^ b) >> 7
    if bit_count <= 8:
        return True
    else:
        return False


def bit_diff9(a, b):
    """
    Returns whether the two numbers differ at exactly nine bit positions.
    """
    if a == b:
        return False
    bit_count = (a ^ b) >> 8
    if bit_count <= 9:
        return True
    else:
        return False


def bit_diff10(a, b):
    """
    Returns whether the two numbers differ at exactly ten bit positions.
    """
    if a == b:
        return False
    bit_count = (a ^ b) >> 9
    if bit_count <= 10:
        return True
    else:
        return False


def bit_diff11(a, b):
    """
    Returns whether the two numbers differ at exactly eleven bit 