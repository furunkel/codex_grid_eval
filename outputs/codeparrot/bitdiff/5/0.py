def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 2 bit positions.
    """
    return (a[0] > b[0] and a[1] > b[1] and a[2] > b[2])


def get_all_bits(bits):
    """
    Returns a list of all bits in the given list.
    """
    return [bit for bit in bits if bit_diff(bit, bits)]


def get_bits_in_range(bits, start, end):
    """
    Returns a list of all bits in the given range.
    """
    return [bit for bit in bits[start:end] if bit_diff(bit, bits)]


def get_bits_in_range_inclusive(bits, start, end):
    """
    Returns a list of all bits in the given range inclusive.
    """
    return [bit for bit in bits[start:end] if bit_diff(bit, bits)]


def get_bits_in_range_exclusive(bits, start, end):
    """
    Returns a list of all bits in the given range exclusive.
    """
    return [bit for bit in bits[start:end] if bit_diff(bit, bits)]


def get_bits_in_range_inclusive_inclusive(bits, start, end):
    """
    Returns a list of all bits in the given range inclusive.
    """
    return [bit for bit in bits[start:end] if bit_diff(bit, bits)]


def get_bits_in_range_exclusive_inclusive(bits, start, end):
    """
    Returns a list of all bits in the given range exclusive.
    """
    return [bit for bit in bits[start:end] if bit_diff(bit, bits)]


def get_bits_in_range_inclusive_exclusive(bits, start, end):
    """
    Returns a list of all bits in the given range inclusive.
    """
    return [bit for bit in bits[start:end] if bit_diff(bit, bits)]


def get_bits_in_range_inclusive_inclusive(bits, start, end):
    """
    Returns a list of all bits in the given range inclusive.
    """
    return [bit for bit in bits[start:end] if bit_diff(bit, bits