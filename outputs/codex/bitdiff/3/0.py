
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 1 bit position.
    """
    return (a ^ b) & -(a ^ b) == a ^ b


def bit_diff_count(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    return bin(a ^ b).count('1')


def bit_diff_count_2(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    c = a ^ b
    count = 0
    while c:
        count += 1
        c &= c - 1
    return count


def bit_diff_count_3(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    c = a ^ b
    count = 0
    while c:
        count += c & 1
        c >>= 1
    return count


def bit_diff_count_4(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    c = a ^ b
    count = 0
    while c:
        count += 1
        c &= c - 1
    return count


def bit_diff_count_5(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    c = a ^ b
    count = 0
    while c:
        count += 1
        c &= c - 1
    return count


def bit_diff_count_6(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    c = a ^ b
    count = 0
    while c:
        count += 1
        c &= c - 1
    return count


def bit_diff_count_7(a, b):
    """
    Returns the number of bit positions in which the two numbers differ.
    """
    c = a ^ b
    count = 0
    while c:
        count += 1
        c &= c - 1
    return count


def bit_diff_count_8(a, b):
    """
    Returns the number of bit positions