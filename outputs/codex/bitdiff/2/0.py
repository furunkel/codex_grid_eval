
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly one bit position.
    """
    return (a ^ b) & -(a ^ b) == a ^ b


def bit_diff_count(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    return bin(a ^ b).count('1')


def bit_diff_count_slow(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    return sum(1 for i in range(64) if (a & (1 << i)) != (b & (1 << i)))


def bit_diff_count_slow2(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    return sum(1 for i in range(64) if (a >> i) & 1 != (b >> i) & 1)


def bit_diff_count_slow3(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    return sum(1 for i in range(64) if (a >> i) ^ (b >> i) & 1)


def bit_diff_count_slow4(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    return sum(1 for i in range(64) if (a >> i) ^ (b >> i))


def bit_diff_count_slow5(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    return sum(1 for i in range(64) if (a >> i) ^ (b >> i) & 1 == 1)


def bit_diff_count_slow6(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    return sum(1 for i in range(64) if (a >> i) ^ (b >> i) & 1)


def bit_diff_count_slow7(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    return sum(1 for i in range(64) if (a