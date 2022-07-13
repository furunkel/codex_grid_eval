def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 3 bit positions.
    """
    return (a[0] != b[0] or
            a[1] != b[1] or
            a[2] != b[2] or
            a[3] != b[3])


def get_bit_diff(a, b):
    """
    Returns the difference between the two numbers.
    """
    return (a[0] - b[0],
            a[1] - b[1],
            a[2] - b[2],
            a[3] - b[3])


def get_bit_diff_str(a, b):
    """
    Returns the difference between the two numbers.
    """
    return (str(a[0] - b[0]),
            str(a[1] - b[1]),
            str(a[2] - b[2]),
            str(a[3] - b[3]))


def get_bit_diff_str_list(a, b):
    """
    Returns the difference between the two numbers.
    """
    return (str(a[0] - b[0]),
            str(a[1] - b[1]),
            str(a[2] - b[2]),
            str(a[3] - b[3]))


def get_bit_diff_str_list_str(a, b):
    """
    Returns the difference between the two numbers.
    """
    return (str(a[0] - b[0]),
            str(a[1] - b[1]),
            str(a[2] - b[2]),
            str(a[3] - b[3]))


def get_bit_diff_str_list_str_list(a, b):
    """
    Returns the difference between the two numbers.
    """
    return (str(a[0] - b[0]),
            str(a[1] - b[1]),
            str(a[2] - b[2]),
            str(a[3] - b[3]))


def get_bit_diff_str_list_str_list_str(a, b):
    """
    Returns the difference between the two numbers.
    """
    return (str(a[0] - b[0