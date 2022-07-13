
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 0 bit positions.
    """
    return a ^ b == 0


def bit_diff_count(a, b):
    """
    Returns the number of bit positions at which the two numbers differ.
    """
    return bin(a ^ b).count('1')


def bit_diff_count_fast(a, b):
    """
    Returns the number of bit positions at which the two numbers differ.
    """
    c = a ^ b
    count = 0
    while c:
        count += 1
        c &= c - 1
    return count


def bit_diff_count_fastest(a, b):
    """
    Returns the number of bit positions at which the two numbers differ.
    """
    c = a ^ b
    count = 0
    while c:
        count += 1
        c &= c - 1
    return count


def bit_diff_count_fastest_2(a, b):
    """
    Returns the number of bit positions at which the two numbers differ.
    """
    c = a ^ b
    count = 0
    while c:
        count += 1
        c &= c - 1
    return count


def bit_diff_count_fastest_3(a, b):
    """
    Returns the number of bit positions at which the two numbers differ.
    """
    c = a ^ b
    count = 0
    while c:
        count += 1
        c &= c - 1
    return count


def bit_diff_count_fastest_4(a, b):
    """
    Returns the number of bit positions at which the two numbers differ.
    """
    c = a ^ b
    count = 0
    while c:
        count += 1
        c &= c - 1
    return count


def bit_diff_count_fastest_5(a, b):
    """
    Returns the number of bit positions at which the two numbers differ.
    """
    c = a ^ b
    count = 0
    while c:
        count += 1
        c &= c - 1
    return count


def bit_diff_count_fastest_6(a, b):
    """
    Returns