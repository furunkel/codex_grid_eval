
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly six bit positions.
    """
    return bin(a^b)[-6:] == "0"*6

def bit_diffs(a, b):
    """
    Returns a list of pairs of numbers, where each pair has the form (bit_diff(a, b), a).
    """
    return [(a, a) if a == b else (bit_diff(a, b), b) for a in range(2**6)]

def bit_diffs_count(a, b):
    """
    Returns the number of pairs of numbers, where each pair has the form (bit_diff(a, b), a).
    """
    return sum(1 for bit_diff, a in bit_diffs(a, b) if bit_diff)

def bit_diffs_count_fast(a, b):
    """
    Returns the number of pairs of numbers, where each pair has the form (bit_diff(a, b), a).
    """
    return sum(1 for bit_diff, a in bit_diffs(a, b) if bit_diff)

def bit_diffs_count_fast2(a, b):
    """
    Returns the number of pairs of numbers, where each pair has the form (bit_diff(a, b), a).
    """
    return sum(1 for bit_diff, a in bit_diffs(a, b) if bit_diff)

def bit_diffs_count_fast3(a, b):
    """
    Returns the number of pairs of numbers, where each pair has the form (bit_diff(a, b), a).
    """
    return sum(1 for bit_diff, a in bit_diffs(a, b) if bit_diff)

def bit_diffs_count_fast4(a, b):
    """
    Returns the number of pairs of numbers, where each pair has the form (bit_diff(a, b), a).
    """
    return sum(1 for bit_diff, a in bit_diffs(a, b) if bit_diff)

def bit_diffs_count_fast5(a, b):
    """
    Returns the number of pairs of numbers, where each pair has the form (bit_diff(a, b), a).
    """
    return sum(1 for bit_diff, a in bit_diffs(a, b) if bit_diff)

def bit_diffs_count_fast6(a, b):
    """
    Returns the number of pairs of numbers, where each pair has the form (bit_diff(a, b), a).
    """
    return sum(1 for bit_diff, a in bit_diffs(a, b) if bit_diff)

def bit_diffs_count_fast7(a, b):
    """
    Returns the number of pairs of numbers, where each pair has the form (bit_diff(a, b), a).
    """
    return sum(1 for bit_diff, a in bit_diffs(a, b) if bit_diff)

def bit_diffs_count_fast8(a, b):
    """
    Returns the number of pairs of numbers, where each pair has the form (bit_diff(a, b), a).
    """
    return sum(1 for bit_diff, a in bit_diffs(a, b) if bit_diff)

def bit_diffs_count_fast9(a, b):
    """