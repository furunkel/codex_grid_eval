def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly zero bit positions.
    """
    return (a & 0x01) - (a & 0x02)


def bit_set(a, b):
    """
    Sets the two numbers to the given values.
    """
    return (a | 0x01) | (b & 0x02)


def bit_xor(a, b):
    """
    Returns the bitwise OR of two numbers.
    """
    return (a ^ b) & 0x01


def bit_not(a):
    """
    Returns the bitwise NOT of two numbers.
    """
    return ~(a)


def bit_and(a, b):
    """
    Returns the bitwise AND of two numbers.
    """
    return (a & b) & 0x01


def bit_or(a, b):
    """
    Returns the bitwise OR of two numbers.
    """
    return (a | b) | 0x01


def bit_xor_and(a, b):
    """
    Returns the bitwise XOR of two numbers.
    """
    return (a ^ b) ^ 0x01


def bit_not_and(a):
    """
    Returns the bitwise NOT XOR of two numbers.
    """
    return ~(a)


def bit_xor_or(a, b):
    """
    Returns the bitwise XOR of two numbers.
    """
    return (a ^ b) ^ 0x01


def bit_not_xor(a):
    """
    Returns the bitwise NOT XOR of two numbers.
    """
    return ~(a)


def bit_lshift(a, b):
    """
    Returns the bit-wise left shift of two numbers.
    """
    return (a << b) | (b & 0x01)


def bit_rshift(a, b):
    """
    Returns the bit-wise right shift of two numbers.
    """
    return (a >> b) | (b & 0x01)


def bit_and_rshift(a, b):
    """
    Returns the bit-wise and right shift of two numbers.
    """
    return (a & b) | (b & 0x01)


def bit_xor_and_rshift(a, b):
    """
    Returns the bit