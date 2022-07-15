
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly fifteen bit positions.
    """
    if a == b:
        return False
    bit_diff = 0
    for bit_position in range(0, 16):
        bit_diff = (bit_diff << 1) | (a & 1)
        a >>= 1
    return bit_diff != 0


def bit_count(n):
    """
    Returns the number of bits necessary to encode the given number
    in binary.
    """
    count = 0
    while n != 0:
        count += 1
        n >>= 1
    return count


def bit_length(n):
    """
    Returns the number of bits necessary to encode the given number
    in decimal.
    """
    count = 0
    while n != 0:
        count += 1
        n >>= 1
    return count


def bit_to_binary(n, num_bits):
    """
    Returns the binary representation of the given number in base 2.
    """
    return bin(n)[2:].zfill(num_bits)


def bit_to_decimal(n, num_bits):
    """
    Returns the decimal representation of the given number in base 2.
    """
    return int(bin(n)[2:].zfill(num_bits), 2)


def bit_to_hex(n, num_bits):
    """
    Returns the hexadecimal representation of the given number in base 2.
    """
    return hex(int(bin(n)[2:].zfill(num_bits), 2))


def bit_to_octal(n, num_bits):
    """
    Returns the octal representation of the given number in base 2.
    """
    return oct(int(bin(n)[2:].zfill(num_bits), 2))


def bit_to_words(n, num_bits):
    """
    Returns the words of the given number in base 2.
    """
    words = []
    while n != 0:
        words.append(n & 1)
        n >>= 1
    return words


def bit_to_bytes(n, num_bits):
    """
    Returns the bytes of the given number in base 2.
    """
    bytes = []
    while n != 0:
        bytes.append(n & 1)
        n >>= 8
    return bytes


def bit_to_int(n, num_bits):
    """
    Returns the integer representation of the given number in base 2.
    """
    return int(bin(n)[2:].zfill(num_bits), 2)


def bit_to_float(n, num_bits):
    """
    Returns the float representation of the given number in base 2.
    """
    return float(bin(n)[2:].zfill(num_bits))


def bit_to_hexfloat(n, num_bits):
    """
    Returns the hexfloat representation of the given number in base 2.
    """
    return hexfloat(bin(n)[2:].zfill(num_bits))


def bit_to_hexfloats(n, num_bits):
    """
    Returns the hexfloats of the given number in base 2.
    """
    return hexfloats(bin