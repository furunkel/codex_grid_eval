
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly zero bit positions.
    """
    return all(a != b for a in six.iterbytes(a) and six.iterbytes(b) and six.iterbytes(a) != six.iterbytes(b))


def bit_flip(a, bit):
    """
    Flips a single bit in ``a``.
    """
    return six.int2byte(six.byte2int(six.bytearray_to_bytes(a)) ^ six.int2byte(bit))


def bit_xor(a, b):
    """
    Returns the bitwise XOR of two numbers.
    """
    return six.int2byte(six.byte2int(six.bytearray_to_bytes(a)) ^ six.int2byte(six.byte2int(six.bytearray_to_bytes(b))))


def bit_or(a, b):
    """
    Returns the bitwise OR of two numbers.
    """
    return six.int2byte(six.byte2int(six.bytearray_to_bytes(a)) | six.int2byte(six.byte2int(six.bytearray_to_bytes(b))))


def bit_and(a, b):
    """
    Returns the bitwise AND of two numbers.
    """
    return six.int2byte(six.byte2int(six.bytearray_to_bytes(a)) & six.int2byte(six.byte2int(six.bytearray_to_bytes(b))))


def bit_not(a):
    """
    Returns the bitwise NOT of a single number.
    """
    return six.int2byte(~six.byte2int(six.bytearray_to_bytes(a)))


def bit_length(a):
    """
    Returns the number of bits necessary to represent ``a`` in binary.
    """
    return len(bin(six.byte2int(a)))


def bit_length_uint(n):
    """
    Returns the number of bits necessary to represent ``n`` in binary.
    """
    return len(bin(n))


def bit_length_int(n):
    """
    Returns the number of bits necessary to represent ``n`` in decimal.
    """
    return len(str(n))


def bit_length_float(n):
    """
    Returns the number of bits necessary to represent ``n`` in decimal.
    """
    return len(str(float(n)))


def bit_length_fractional(n):
    """
    Returns the number of bits necessary to represent ``n`` in decimal.
    """
    return len(str(Fraction(n)))


def bit_length_complex(n):
    """
    Returns the number of bits necessary to represent ``n`` in decimal.
    """
    return len(str(Complex(int(n))))


def bit_length_mpq(n):
    """
    Returns the number of bits necessary to represent ``n`` in decimal.
    """
    return len(str(mpq(n)))


def bit_length_mpqint(n):
    """
    Returns the number of bits necessary to represent ``n`` in decimal.
    """
