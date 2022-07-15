
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 11 bit positions.
    """
    return bin(a^b)[-11:] == '11111111'


def bit_flip(a):
    """
    Returns the bitwise negation of a, i.e. the bitwise complement of a.
    """
    return ~a


def bit_not(a):
    """
    Returns the bitwise inverse of a (a & ~a).
    """
    return a^~a


def bit_or(a, b):
    """
    Returns the bitwise OR of a and b.
    """
    return a|b


def bit_and(a, b):
    """
    Returns the bitwise AND of a and b.
    """
    return a&b


def bit_xor(a, b):
    """
    Returns the bitwise XOR of a and b.
    """
    return a^b


def bit_shl(a, b):
    """
    Returns the bitwise left shift of a and b.
    """
    return a<<b


def bit_shr(a, b):
    """
    Returns the bitwise right shift of a and b.
    """
    return a>>b


def bit_xorshift(a, b):
    """
    Returns the bitwise XOR shift of a and b.
    """
    return a^b


def bit_rol(a, b):
    """
    Returns the bitwise right rotation of a and b.
    """
    return a>>b|a<<(32-b)


def bit_ror(a, b):
    """
    Returns the bitwise left rotation of a and b.
    """
    return a<<b|a>>(32-b)


def bit_band(a, b):
    """
    Returns the bitwise AND of a and b, i.e. the bitwise AND of (a & b).
    """
    return a&b


def bit_rshift(a, b):
    """
    Returns the bitwise right shift of a and b, i.e. the bitwise right shift of a >> b.
    """
    return a>>b


def bit_lshift(a, b):
    """
    Returns the bitwise left shift of a and b, i.e. the bitwise left shift of a << b.
    """
    return a<<b


def bit_bandnot(a, b):
    """
    Returns the bitwise AND of a and b, i.e. the bitwise AND of (a & b).
    """
    return a&b


def bit_rshiftnot(a, b):
    """
    Returns the bitwise right shift of a and b, i.e. the bitwise right shift of a >> b.
    """
    return a>>b


def bit_lshiftnot(a, b):
    """
    Returns the bitwise left shift of a and b, i.e. the bitwise left shift of a << b.
    """
    return a<<b


def bit_bandnot(a, b):
    """
    Returns the bitwise AND of a and b, i.e. the bitwise AND of (