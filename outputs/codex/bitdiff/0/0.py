
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly zero bit positions.
    """
    return a ^ b == 0


def bit_diff_count(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    return bin(a ^ b).count('1')


def bit_diff_count_slow(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    count = 0
    for i in range(32):
        if (a & (1 << i)) != (b & (1 << i)):
            count += 1
    return count


def bit_diff_count_slow2(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    count = 0
    for i in range(32):
        if (a >> i) & 1 != (b >> i) & 1:
            count += 1
    return count


def bit_diff_count_slow3(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    count = 0
    for i in range(32):
        if (a >> i) ^ (b >> i) & 1:
            count += 1
    return count


def bit_diff_count_slow4(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    count = 0
    for i in range(32):
        if (a >> i) ^ (b >> i):
            count += 1
    return count


def bit_diff_count_slow5(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    count = 0
    for i in range(32):
        if (a >> i) ^ (b >> i) & 1:
            count += 1
    return count


def bit_diff_count_slow6(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    count = 0
    for i in range(32):
        if (a >> i) ^ (b >> i):
            count += 1