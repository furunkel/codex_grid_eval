
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly eleven bit positions.
    """
    return bin(a^b)[-11:]


def bit_flip(a):
    """
    Returns the bitwise negation of a, i.e. the bitwise complement of a.
    """
    return ~a


def bit_flip_inverse(a):
    """
    Returns the bitwise inversion of a, i.e. the bitwise negation of a.
    """
    return a


def bit_flip_complement(a):
    """
    Returns the bitwise complement of a, i.e. the bitwise negation of a.
    """
    return ~a


def bit_flip_to_signed_int(a):
    """
    Returns the bitwise representation of a, but as a signed integer.
    """
    return a if a < 0 else (a ^ 0xffffffff) + 1


def bit_flip_to_unsigned_int(a):
    """
    Returns the bitwise representation of a, but as an unsigned integer.
    """
    return a if a < 0 else a


def bit_flip_to_signed_int_in_range(a, low, high):
    """
    Returns the bitwise representation of a, but as a signed integer in
    the range [low, high].
    """
    return bit_flip_to_signed_int(a) if a < low else high


def bit_flip_to_unsigned_int_in_range(a, low, high):
    """
    Returns the bitwise representation of a, but as an unsigned integer in
    the range [low, high].
    """
    return bit_flip_to_unsigned_int(a) if a < low else low


def bit_flip_to_signed_int_in_range_inclusive(a, low, high):
    """
    Returns the bitwise representation of a, but as a signed integer in
    the range [low, high] inclusive.
    """
    return bit_flip_to_signed_int_in_range(a, low, high) if a < low else low


def bit_flip_to_unsigned_int_in_range_inclusive(a, low, high):
    """
    Returns the bitwise representation of a, but as an unsigned integer in
    the range [low, high] inclusive.
    """
    return bit_flip_to_unsigned_int_in_range(a, low, high) if a < low else high


def bit_flip_to_signed_int_in_range_exclusive(a, low, high):
    """
    Returns the bitwise representation of a, but as a signed integer in
    the range [low, high] exclusive.
    """
    return bit_flip_to_signed_int_in_range(a, low, high) if a < low else high - 1


def bit_flip_to_unsigned_int_in_range_exclusive(a, low, high):
    """
    Returns the bitwise representation of a, but as an unsigned integer in
    the range [low, high] exclusive.
    """
    return bit_flip_to_unsigned_int_in_range(a, low, high) if a < low else high - 1


def bit_flip_to_signed_int_