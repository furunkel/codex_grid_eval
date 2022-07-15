
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 6 bit positions.
    """
    return bin(a^b)[-6:] == "1111"

def bit_flip(a):
    """
    Flips the 6th bit of a into the 5th and 6th bits of b.
    """
    return (a<<1) ^ (a>>63)

def bit_xor(a, b):
    """
    Returns the bitwise XOR of two numbers.
    """
    return a ^ b

def bit_and(a, b):
    """
    Returns the bitwise AND of two numbers.
    """
    return a & b

def bit_or(a, b):
    """
    Returns the bitwise OR of two numbers.
    """
    return a | b

def bit_not(a):
    """
    Returns the bitwise NOT of a number.
    """
    return ~a

def bit_shl(a, b):
    """
    Returns the bitwise left shift of a number by the given amount.
    """
    return a << b

def bit_shr(a, b):
    """
    Returns the bitwise right shift of a number by the given amount.
    """
    return a >> b

def bit_rol(a, b):
    """
    Returns the bitwise right rotation of the given number by the given amount.
    """
    return a >> b | a << 32 - b

def bit_ror(a, b):
    """
    Returns the bitwise right rotation of the given number by the given amount.
    """
    return a << b | a >> 32 - b

def bit_band(a, b):
    """
    Returns the bitwise AND of the two numbers where the 6th bit is the same in both.
    """
    return a & b

def bit_rshift(a, b):
    """
    Returns the bitwise right shift of a number by the given amount.
    """
    return a >> b

def bit_lshift(a, b):
    """
    Returns the bitwise left shift of a number by the given amount.
    """
    return a << b

def bit_bandnot(a, b):
    """
    Returns the bitwise AND of the two numbers where the 6th bit is the same in both.
    """
    return ~(a & b)

def bit_rshiftnot(a, b):
    """
    Returns the bitwise right shift of a number by the given amount.
    """
    return a >> b

def bit_lshiftnot(a, b):
    """
    Returns the bitwise left shift of a number by the given amount.
    """
    return a << b

def bit_bandnot(a, b):
    """
    Returns the bitwise AND of the two numbers where the 6th bit is the same in both.
    """
    return ~(a & b)

def bit_rshiftnot(a, b):
    """
    Returns the bitwise right shift of a number by the given amount.
    """
    return a 