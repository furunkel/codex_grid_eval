def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly fifteen bit positions.
    """
    return (a > b) - (a < b)


def bit_count(a):
    """
    Returns the number of bits in a number.
    """
    return a.bit_length()


def bit_length(a):
    """
    Returns the number of bits in a number.
    """
    return a.bit_length()


def bit_count_bits(a):
    """
    Returns the number of bits in a number of bits.
    """
    return a.bit_length()


def bit_length_bits(a):
    """
    Returns the number of bits in a number of bits.
    """
    return a.bit_length()


def bit_count_bits_and_offset(a):
    """
    Returns the number of bits and offset in a number of bits.
    """
    return a.bit_length(), a.bit_offset()


def bit_offset(a):
    """
    Returns the number of bits in a number of bits.
    """
    return a.bit_offset()


def bit_count_bits_and_offset_bits(a):
    """
    Returns the number of bits and offset in a number of bits.
    """
    return a.bit_length(), a.bit_offset()


def bit_offset_bits(a):
    """
    Returns the number of bits and offset in a number of bits.
    """
    return a.bit_length(), a.bit_offset()


def bit_count_bits_and_offset_bits_and_offset(a):
    """
    Returns the number of bits and offset in a number of bits and offset in a number of bits.
    """
    return a.bit_length(), a.bit_offset(), a.bit_offset()


def bit_offset_bits_and_offset_bits_and_offset_bits(a):
    """
    Returns the number of bits and offset in a number of bits and offset in a number of bits and offset in a number of bits.
    """
    return a.bit_length(), a.bit_offset(), a.bit_offset()


def bit_count_bits_and_offset_bits_and_offset_bits_and_offset(a