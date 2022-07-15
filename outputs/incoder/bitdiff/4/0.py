
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly two bit positions.
    """
    return bin(a^b)[2:].count('1')

def bit_diffs(a, b):
    """
    Returns a list of the differences between the two numbers.
    """
    return [bit_diff(a, b) for a in range(32)]

def bit_flips(a, b):
    """
    Returns a list of the bit flips between the two numbers.
    """
    return [bit_diff(b, a) for a in range(32)]

def bit_flips_diff(a, b):
    """
    Returns a list of the bit flips between the two numbers and the differences
    between those bit flips.
    """
    return bit_diffs(a, b) + bit_flips(a, b)

def bit_flips_diffs(a, b):
    """
    Returns a list of the bit flips between the two numbers and the differences
    between those bit flips.
    """
    return bit_diffs(a, b) + bit_flips(a, b)

def bit_flips_diffs_diff(a, b):
    """
    Returns a list of the bit flips between the two numbers and the differences
    between those bit flips and the differences between those bit flips.
    """
    return bit_diffs(a, b) + bit_flips(a, b) + bit_flips(b, a)

def bit_flips_diffs_diffs(a, b):
    """
    Returns a list of the bit flips between the two numbers and the differences
    between those bit flips and the differences between those bit flips.
    """
    return bit_diffs(a, b) + bit_flips(a, b) + bit_flips(b, a)

def bit_flips_diffs_diffs_diff(a, b):
    """
    Returns a list of the bit flips between the two numbers and the differences
    between those bit flips and the differences between those bit flips.
    """
    return bit_diffs(a, b) + bit_flips(a, b) + bit_flips(b, a) + bit_flips(a, b)

def bit_flips_diffs_diffs_diffs(a, b):
    """
    Returns a list of the bit flips between the two numbers and the differences
    between those bit flips and the differences between those bit flips.
    """
    return bit_diffs(a, b) + bit_flips(a, b) + bit_flips(b, a) + bit_flips(a, b)

def bit_flips_diffs_diffs_diffs_diff(a, b):
    """
    Returns a list of the bit flips between the two numbers and the differences
    between those bit flips and the differences between those bit flips.
    """
    return bit_diffs(a, b) + bit_flips(a, b) + bit_flips(b, a) + bit_flips(a, b)

def bit_flips_diffs_diffs_diffs_diffs(a, b):
    """
    Returns a list of the bit flips between the two numbers and the differences
    between those bit flips and the differences between those bit flip