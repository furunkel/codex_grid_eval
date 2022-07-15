
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly four bit positions.
    """
    return bin(a^b)[-4:] == "100"

def bit_diffs(a, b):
    """
    Returns the number of bits differed in two numbers.
    """
    return sum((bit_diff(a, b) for _ in xrange(4)))

def bit_flips(a, b):
    """
    Returns the number of bit flips in two numbers.
    """
    return sum((bit_flip(a, b) for _ in xrange(4)))

def bit_flip(a, b):
    """
    Returns whether the two numbers differ at exactly two bit positions.
    """
    return bin(a^b)[-2:] == "01"

def bit_flips(a, b):
    """
    Returns the number of bit flips in two numbers.
    """
    return sum((bit_flip(a, b) for _ in xrange(2)))

def bit_flips_diff(a, b):
    """
    Returns the number of bit flips differed in two numbers.
    """
    return sum((bit_flips_diff(a, b) for _ in xrange(2)))

def bit_flips_diffs(a, b):
    """
    Returns the number of bit flips differed in two numbers.
    """
    return sum((bit_flips_diff(a, b) for _ in xrange(2)))

def bit_flips_diffs_diff(a, b):
    """
    Returns the number of bit flips differed in two numbers.
    """
    return sum((bit_flips_diff(a, b) for _ in xrange(2)))

def bit_flips_diffs_diffs(a, b):
    """
    Returns the number of bit flips differed in two numbers.
    """
    return sum((bit_flips_diff(a, b) for _ in xrange(2)))

def bit_flips_diffs_diffs_diff(a, b):
    """
    Returns the number of bit flips differed in two numbers.
    """
    return sum((bit_flips_diff(a, b) for _ in xrange(2)))

def bit_flips_diffs_diffs_diffs(a, b):
    """
    Returns the number of bit flips differed in two numbers.
    """
    return sum((bit_flips_diff(a, b) for _ in xrange(2)))

def bit_flips_diffs_diffs_diffs_diff(a, b):
    """
    Returns the number of bit flips differed in two numbers.
    """
    return sum((bit_flips_diff(a, b) for _ in xrange(2)))

def bit_flips_diffs_diffs_diffs_diffs(a, b):
    """
    Returns the number of bit flips differed in two numbers.
    """
    return sum((bit_flips_diff(a, b) for _ in xrange(2)))

def bit_flips_diffs_diffs_diffs_diffs_diff(a, b):
    """
    Returns the number of bit flips differed in two numbers.
    """
    return sum((bit_flips_diff(a, b) for _ in 