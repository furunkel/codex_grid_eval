
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 11 bit positions.
    """
    diff = 0
    for i in range(11):
        if ((a >> i) != (b >> i)) and ((a >> i) != 0):
            diff += 1
    return diff


def bit_length(a):
    """
    Returns the number of bits required to store an integer.
    """
    return len(bin(a)) - 2


def bit_length_in_bits(a):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length(a) * 8


def bit_length_of_int(i):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(i)


def bit_length_of_float(f):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(f)


def bit_length_of_double(d):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(d)


def bit_length_of_string(x):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(len(x))


def bit_length_of_vector(v):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(len(v))


def bit_length_of_set(s):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(len(s))


def bit_length_of_map(m):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(len(m))


def bit_length_of_pair(p):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(len(p))


def bit_length_of_string(s):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(len(s))


def bit_length_of_vector(v):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(len(v))


def bit_length_of_set(s):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(len(s))


def bit_length_of_map(m):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(len(m))


def bit_length_of_pair(p):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(len(p))


def bit_length_of_string(s):
    """
    Returns the number of bits required to store an integer.
    """
    return bit_length_in_bits(len(s))


def bit_length_of_vector(v):
    """
    Returns the number of bits 