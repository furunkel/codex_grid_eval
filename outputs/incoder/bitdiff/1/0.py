
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 0 bit positions.
    """
    return a ^ b == 0


def bit_flip(a):
    """
    Returns the bitwise negation of a, i.e. the complement of a.
    """
    return ~a


def bit_not(a):
    """
    Returns the bitwise inverse of a, i.e. the opposite of a.
    """
    return a


def bit_or(a, b):
    """
    Returns the bitwise OR of two numbers a and b.
    """
    return a | b


def bit_and(a, b):
    """
    Returns the bitwise AND of two numbers a and b.
    """
    return a & b


def bit_xor(a, b):
    """
    Returns the bitwise XOR of two numbers a and b.
    """
    return a ^ b


def bit_shl(a, b):
    """
    Returns the bitwise left shift of a number a by b bits.
    """
    return a << b


def bit_shr(a, b):
    """
    Returns the bitwise right shift of a number a by b bits.
    """
    return a >> b


def bit_xorshift(a, b):
    """
    Returns the bitwise XOR shift of a number a by b bits.
    """
    return a ^ (a >> b)


def bit_rol(a, b):
    """
    Returns the bitwise right rotation of b bits in a number a.
    """
    return a >> b | a << 32 - (b % 32)


def bit_ror(a, b):
    """
    Returns the bitwise left rotation of b bits in a number a.
    """
    return a << b | a >> 32 - (b % 32)


def bit_test(a, bit):
    """
    Returns 1 if the bit is set in a number a, 0 otherwise.
    """
    return a & (1 << bit) != 0


def bit_set(a, bit):
    """
    Sets the bit in a number a to 1.
    """
    return a | (1 << bit)


def bit_clear(a, bit):
    """
    Sets the bit in a number a to 0.
    """
    return a & ~(1 << bit)


def bit_testall(a, bit):
    """
    Returns 1 if the bit in a is set in a number a, 0 otherwise.
    """
    return a & bit_test(a, bit)


def bit_setall(a, bit):
    """
    Sets the bit in a number a to 1.
    """
    return a | bit_set(a, bit)


def bit_clearall(a, bit):
    """
    Sets the bit in a number a to 0.
    """
    return a & ~bit_clear(a, bit)


def bit_flipall(a):
    """
    Returns the bitwise negation of all bits in a number a.
    """
    return bit_not(bit_test(a, 0))


def bit_