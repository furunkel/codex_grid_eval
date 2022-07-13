
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 6 bit positions.
    """
    return bin(a^b)[-6:] == "1111"

def bit_flip(a):
    """
    Returns the bitwise negation of a, i.e. the complement of a.
    """
    return bin(~a)[-6:] == "1111"

def bit_not(a):
    """
    Returns the bitwise negation of a, i.e. the complement of a.
    """
    return bin(~a)[-6:] == "1111"

def bit_or(a, b):
    """
    Returns the bitwise OR of two numbers.
    """
    return bin(a|b)[-6:] == "1111"

def bit_and(a, b):
    """
    Returns the bitwise AND of two numbers.
    """
    return bin(a&b)[-6:] == "1111"

def bit_xor(a, b):
    """
    Returns the bitwise XOR of two numbers.
    """
    return bin(a^b)[-6:] == "1111"

def bit_not(a):
    """
    Returns the bitwise negation of a, i.e. the complement of a.
    """
    return bin(~a)[-6:] == "1111"

def bit_shift(a, n):
    """
    Returns the bitwise left shift of a number by n.
    """
    return bin(a<<n)[-6:] == "1111"

def bit_test(a, n, bit):
    """
    Returns whether the bit at position n in the binary representation of a
    number is set.
    """
    return bin(a>>n)[-6:] == "1111"

def bit_clear(a, n, bit):
    """
    Sets a bit in the binary representation of a number.
    """
    return bin(a<<n)[-6:] == "1111"

def bit_flip(a):
    """
    Returns the bitwise negation of a, i.e. the complement of a.
    """
    return bin(~a)[-6:] == "1111"

def bit_not(a):
    """
    Returns the bitwise negation of a, i.e. the complement of a.
    """
    return bin(~a)[-6:] == "1111"

def bit_or(a, b):
    """
    Returns the bitwise OR of two numbers.
    """
    return bin(a|b)[-6:] == "1111"

def bit_and(a, b):
    """
    Returns the bitwise AND of two numbers.
    """
    return bin(a&b)[-6:] == "1111"

def bit_xor(a, b):
    """
    Returns the bitwise XOR of two numbers.
    """
    return bin(a^b)[-6:] == "1111"

def bit_not(a):
    """
    Returns the bitwise negation of a, i.e. the complement of a.
    """
    return bin(~a)[-6:] == "1111"

def bit_shift(a, n):
    """
    Return