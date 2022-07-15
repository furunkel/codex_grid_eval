
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly five bit positions.
    """
    if a == b:
        return False
    bit_count = (a ^ b) >> 3
    if bit_count == 5:
        return True
    else:
        return False

def bit_count(n):
    """
    Returns the number of bits required to represent n.
    """
    return bin(n).count('1')

def bit_length(n):
    """
    Returns the number of bits required to represent n.
    """
    return bit_count(n) - 1

def bit_to_int(n):
    """
    Returns the integer n represented by exactly five bits.
    """
    return n >> 3

def int_to_bit(n):
    """
    Returns the five bit representation of n.
    """
    return n & 0b1111

def int_to_bit_length(n):
    """
    Returns the number of bits required to represent n.
    """
    return bit_count(n)

def bit_to_int(n):
    """
    Returns the integer n represented by exactly five bits.
    """
    return n >> 3

def int_to_bit_length(n):
    """
    Returns the number of bits required to represent n.
    """
    return bit_count(n)

def bit_length(n):
    """
    Returns the number of bits required to represent n.
    """
    return bit_count(n) - 1

def bit_to_int(n):
    """
    Returns the integer n represented by exactly five bits.
    """
    return n >> 3

def int_to_bit_length(n):
    """
    Returns the number of bits required to represent n.
    """
    return bit_count(n)

def bit_length(n):
    """
    Returns the number of bits required to represent n.
    """
    return bit_count(n) - 1

def bit_to_int(n):
    """
    Returns the integer n represented by exactly five bits.
    """
    return n >> 3

def int_to_bit_length(n):
    """
    Returns the number of bits required to represent n.
    """
    return bit_count(n)

def bit_length(n):
    """
    Returns the number of bits required to represent n.
    """
    return bit_count(n) - 1

def bit_to_int(n):
    """
    Returns the integer n represented by exactly five bits.
    """
    return n >> 3

def int_to_bit_length(n):
    """
    Returns the number of bits required to represent n.
    """
    return bit_count(n)

def bit_length(n):
    """
    Returns the number of bits required to represent n.
    """
    return bit_count(n) - 1

def bit_to_int(n):
    """
    Returns the integer n represented by exactly five bits.
    """
    return n >> 3

def int_to_bit_length(n):
    """
    Returns the number of bits required to represent n.
    """
    return bit_count(n)

def bit_length(n):
    """
    Returns the number of bits required to represent n.
