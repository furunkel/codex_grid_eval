
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 5 bit positions.
    """
    return bin(a^b)[-5:] == '1111'


def bit_flip(a):
    """
    Returns the bitwise negation of a, i.e. the complement of a.
    """
    return ~a


def bit_not(a):
    """
    Returns the bitwise inverse of a (i.e. ~a).
    """
    return a


def bit_or(a, b):
    """
    Returns the bitwise OR of a and b.
    """
    return a | b


def bit_and(a, b):
    """
    Returns the bitwise AND of a and b.
    """
    return a & b


def bit_xor(a, b):
    """
    Returns the bitwise XOR of a and b.
    """
    return a ^ b


def bit_shl(a, b):
    """
    Returns the bitwise left shift of a and b.
    """
    return a << b


def bit_shr(a, b):
    """
    Returns the bitwise right shift of a and b.
    """
    return a >> b


def bit_xorshift(a, b):
    """
    Returns the bitwise XOR shift of a and b.
    """
    return a ^ (b << a)


def bit_rol(a, b):
    """
    Returns the bitwise right logical shift of a and b.
    """
    return a >> b


def bit_ror(a, b):
    """
    Returns the bitwise right logical OR of a and b.
    """
    return a | (b << abs(b - 1))


def bit_not(a):
    """
    Returns the bitwise inverse of a (i.e. ~a).
    """
    return a


def bit_and(a, b):
    """
    Returns the bitwise AND of a and b.
    """
    return a & b


def bit_or(a, b):
    """
    Returns the bitwise OR of a and b.
    """
    return a | b


def bit_xor(a, b):
    """
    Returns the bitwise XOR of a and b.
    """
    return a ^ b


def bit_shl(a, b):
    """
    Returns the bitwise left shift of a and b.
    """
    return a << b


def bit_shr(a, b):
    """
    Returns the bitwise right shift of a and b.
    """
    return a >> b


def bit_xorshift(a, b):
    """
    Returns the bitwise XOR shift of a and b.
    """
    return a ^ (b << a)


def bit_rol(a, b):
    """
    Returns the bitwise right logical shift of a and b.
    """
    return a >> b


def bit_ror(a, b):
    """
    Returns the bitwise right logical OR of a and b.
    """
    return a | (b << abs(b - 1))


def bit_not(a):
    """
    Returns the bitwise inverse of a (i.e. ~a).
    """