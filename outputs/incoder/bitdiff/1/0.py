
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 0 bit positions.
    """
    return a == b or not (a ^ b)

def bit_length(n):
    """
    Returns the number of bits required to represent a number in binary.
    """
    return len(bin(n)) - 2

def bit_count(n):
    """
    Returns the number of bits required to represent a number in binary.
    """
    return n.bit_length()

def bit_to_int(n):
    """
    Returns the integer that represents the bit string in binary.
    """
    return int(n, 2)

def int_to_bit(n):
    """
    Returns the bit string that represents the integer n.
    """
    return bin(n)[2:]

def int_to_bytes(n):
    """
    Returns the byte string that represents the integer n.
    """
    return int_to_bit(n).zfill(bit_length(n))

def bytes_to_int(s):
    """
    Returns the integer that represents the byte string s in binary.
    """
    return int(s, 2)

def bytes_to_bit(s):
    """
    Returns the bit string that represents the byte string s in binary.
    """
    return int_to_bit(bytes_to_int(s))

def bit_to_bytes(n):
    """
    Returns the byte string that represents the bit string in binary.
    """
    return int_to_bytes(bit_to_int(n))

def bit_to_int(n):
    """
    Returns the integer that represents the bit string in binary.
    """
    return bytes_to_int(bit_to_bytes(n))

def int_to_bytes(n):
    """
    Returns the byte string that represents the integer n.
    """
    return int_to_bit(n).zfill(bit_length(n))

def bytes_to_int(s):
    """
    Returns the integer that represents the byte string s in binary.
    """
    return int(s, 2)

def bytes_to_bit(s):
    """
    Returns the bit string that represents the byte string s in binary.
    """
    return int_to_bit(bytes_to_int(s))

def bit_to_bytes(n):
    """
    Returns the byte string that represents the bit string in binary.
    """
    return int_to_bytes(bit_to_int(n))

def bit_to_int(n):
    """
    Returns the integer that represents the bit string in binary.
    """
    return bytes_to_int(bit_to_bytes(n))

def int_to_bytes(n):
    """
    Returns the byte string that represents the integer n.
    """
    return int_to_bit(n).zfill(bit_length(n))

def bytes_to_int(s):
    """
    Returns the integer that represents the byte string s in binary.
    """
    return int(s, 2)

def bytes_to_bit(s):
    """
    Returns the bit string that represents the byte string s in binary.
    """
    return int_to_bit(bytes_to_int(s))

def bit_to_bytes(n):
    """
    Returns the byte string 