
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 2 bit positions.
    """
    return bin(a ^ b).count('1') == 2


def find_diff(a, b):
    """
    Returns the bit position where the two numbers differ.
    """
    return bin(a ^ b).find('1')


def find_diff_bit(a, b):
    """
    Returns the bit position where the two numbers differ.
    """
    return bin(a ^ b)[2:].find('1')


def find_diff_bit_2(a, b):
    """
    Returns the bit position where the two numbers differ.
    """
    return bin(a ^ b)[2:].index('1')


def find_diff_bit_3(a, b):
    """
    Returns the bit position where the two numbers differ.
    """
    return bin(a ^ b).index('1') - 2


def find_diff_bit_4(a, b):
    """
    Returns the bit position where the two numbers differ.
    """
    return bin(a ^ b).rindex('1') - 2


def find_diff_bit_5(a, b):
    """
    Returns the bit position where the two numbers differ.
    """
    return bin(a ^ b).rindex('1') - 2


def find_diff_bit_6(a, b):
    """
    Returns the bit position where the two numbers differ.
    """
    return bin(a ^ b).rindex('1') - 2


def find_diff_bit_7(a, b):
    """
    Returns the bit position where the two numbers differ.
    """
    return bin(a ^ b).rindex('1') - 2


def find_diff_bit_8(a, b):
    """
    Returns the bit position where the two numbers differ.
    """
    return bin(a ^ b).rindex('1') - 2


def find_diff_bit_9(a, b):
    """
    Returns the bit position where the two numbers differ.
    """
    return bin(a ^ b).rindex('1') - 2


def find_diff_bit_10(a, b):
   