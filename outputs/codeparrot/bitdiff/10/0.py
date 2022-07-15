def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly five bit positions.
    """
    return (a[0] > b[0] and a[1] > b[1] and a[2] > b[2] and
            a[3] > b[3] and a[4] > b[4] and a[5] > b[5])


def get_all_bits(num):
    """
    Returns a list of all the bits in the given number.
    """
    return [bit for bit in range(num)]


def get_bit_diff(num1, num2):
    """
    Returns the difference between two numbers.
    """
    return (num1[0] - num2[0]) * (num1[1] - num2[1]) - (num1[2] - num2[2]) * (num1[3] - num2[3])


def get_bit_diff_list(num1, num2):
    """
    Returns a list of all the bits in the given number.
    """
    return [bit for bit in range(num1[0], num2[0] + num1[2] + num2[2])]


def get_bit_diff_list_2(num1, num2):
    """
    Returns a list of all the bits in the given number.
    """
    return [bit for bit in range(num1[0], num2[0] + num1[2] + num2[2])]


def get_bit_diff_list_3(num1, num2):
    """
    Returns a list of all the bits in the given number.
    """
    return [bit for bit in range(num1[0], num2[0] + num1[2] + num2[2] + num1[3])]


def get_bit_diff_list_4(num1, num2):
    """
    Returns a list of all the bits in the given number.
    """
    return [bit for bit in range(num1[0], num2[0] + num1[2] + num2[2] + num1[3] + num2[3] + num1[4] + num2[4] + num1[5] + num