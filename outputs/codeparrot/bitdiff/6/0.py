def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly three bit positions.
    """
    return (a[0] > b[0] and a[1] > b[1] and a[2] > b[2])


def get_bit_diff(a, b):
    """
    Returns the difference between the two numbers.
    """
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def get_bit_diff_str(a, b):
    """
    Returns the difference between the two numbers.
    """
    return "%s%s" % (get_bit_diff(a, b), get_bit_diff(b, a))


def get_bit_diff_str_list(a, b):
    """
    Returns the difference between the two numbers.
    """
    return "%s%s" % (get_bit_diff_str(a, b), get_bit_diff_str(b, a))


def get_bit_diff_str_list_list(a, b):
    """
    Returns the difference between the two numbers.
    """
    return "%s%s" % (get_bit_diff_str_list(a, b), get_bit_diff_str_list(b, a))


def get_bit_diff_str_list_list(a, b):
    """
    Returns the difference between the two numbers.
    """
    return "%s%s" % (get_bit_diff_str_list_list(a, b), get_bit_diff_str_list_list(b, a))


def get_bit_diff_str_list_list(a, b):
    """
    Returns the difference between the two numbers.
    """
    return "%s%s" % (get_bit_diff_str_list_list(a, b), get_bit_diff_str_list_list(b, a))


def get_bit_diff_str_list_list(a, b):
    """
    Returns the difference between the two numbers.
    """
    return "%s%s" % (get_bit_diff_str_list_list(a, b), get_bit_diff_