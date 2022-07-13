
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly four bit positions.
    """
    diff = 0
    mask = 0xF
    for x, y in zip(a, b):
        diff |= (x ^ y) & mask
        mask >>= 4
    return diff


def bit_diffs(a, b):
    """
    Returns a list of pairs of numbers, where each pair has its bit diff
    exactly four positions.
    """
    diffs = []
    mask = 0xF
    for x, y in zip(a, b):
        diff |= (x ^ y) & mask
        mask >>= 4
        if diff:
            diffs.append((diff, x, y))
    return diffs


def bit_diffs_equal(a, b):
    """
    Returns True if all the pairs of numbers in ``bit_diffs(a, b)`` have
    the same bit diff, False otherwise.
    """
    return len(set(bit_diffs(a, b))) == 1


def bit_diffs_equal(a, b):
    """
    Returns True if all the pairs of numbers in ``bit_diffs(a, b)`` have
    the same bit diff, False otherwise.
    """
    return len(set(bit_diffs(a, b))) == 1


def bit_diffs_equal(a, b):
    """
    Returns True if all the pairs of numbers in ``bit_diffs(a, b)`` have
    the same bit diff, False otherwise.
    """
    return len(set(bit_diffs(a, b))) == 1


def bit_diffs_equal(a, b):
    """
    Returns True if all the pairs of numbers in ``bit_diffs(a, b)`` have
    the same bit diff, False otherwise.
    """
    return len(set(bit_diffs(a, b))) == 1


def bit_diffs_equal(a, b):
    """
    Returns True if all the pairs of numbers in ``bit_diffs(a, b)`` have
    the same bit diff, False otherwise.
    """
    return len(set(bit_diffs(a, b))) == 1


def bit_diffs_equal(a, b):
    """
    Returns True if all the pairs of numbers in ``bit_diffs(a, b)`` have
    the same bit diff, False otherwise.
    """
    return len(set(bit_diffs(a, b))) == 1


def bit_diffs_equal(a, b):
    """
    Returns True if all the pairs of numbers in ``bit_diffs(a, b)`` have
    the same bit diff, False otherwise.
    """
    return len(set(bit_diffs(a, b))) == 1


def bit_diffs_equal(a, b):
    """
    Returns True if all the pairs of numbers in ``bit_diffs(a, b)`` have
    the same bit diff, False otherwise.
    """
    return len(set(bit_diffs(a, b))) == 1


def bit_diffs_equal(a, b):
    """
    Returns True if all the pairs of numbers in ``bit_diffs(a, b)`` have
    the same bit diff, False otherwise.
