
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 4 bit positions.
    """
    return bin(a^b)[-4:] == "111"


def bit_diffs(a, b, n=4):
    """
    Returns the number of bit differences between two numbers.
    """
    return sum((bit_diff(a, b) for _ in xrange(n)))


def bit_flips(a, b, n=4):
    """
    Returns the number of bit flips between two numbers.
    """
    return sum((bit_flip(a, b) for _ in xrange(n)))


def bit_flip(a, b, bits=4):
    """
    Returns the number of bit flips between two numbers.
    """
    return sum((1 << (bits-i-1) if a >> i & 1 else 0 for i in xrange(bits)))


def bit_flips(a, b, n=4):
    """
    Returns the number of bit flips between two numbers.
    """
    return sum((bit_flip(a, b) for _ in xrange(n)))


def bit_flips_diff(a, b, bits=4):
    """
    Returns the number of bit flips between two numbers.
    """
    return sum((1 << (bits-i-1) if a >> i & 1 else 0 for i in xrange(bits)))


def bit_flips_diffs(a, b, n=4):
    """
    Returns the number of bit flips between two numbers.
    """
    return sum((bit_flips_diff(a, b) for _ in xrange(n)))


def bit_flips_diffs_diff(a, b, bits=4):
    """
    Returns the number of bit flips between two numbers.
    """
    return sum((1 << (bits-i-1) if a >> i & 1 else 0 for i in xrange(bits)))


def bit_flips_diffs_diffs(a, b, n=4):
    """
    Returns the number of bit flips between two numbers.
    """
    return sum((bit_flips_diffs_diff(a, b) for _ in xrange(n)))


def bit_flips_diffs_diffs_diff(a, b, bits=4):
    """
    Returns the number of bit flips between two numbers.
    """
    return sum((1 << (bits-i-1) if a >> i & 1 else 0 for i in xrange(bits)))


def bit_flips_diffs_diffs_diffs(a, b, n=4):
    """
    Returns the number of bit flips between two numbers.
    """
    return sum((bit_flips_diffs_diffs_diff(a, b) for _ in xrange(n)))


def bit_flips_diffs_diffs_diffs_diff(a, b, bits=4):
    """
    Returns the number of bit flips between two numbers.
    """
    return sum((1 << (bits-i-1) if a >> i & 1 else 0 for i in xrange(bits)))


def bit_flips_diffs_diffs_diffs_diffs(a, b, n=4):
    """
    Returns the number of bit flips between two numbers.
    """
    return sum((bit_flips_diffs_diffs_diffs_diff(a, b) for _ in xrange(n)))