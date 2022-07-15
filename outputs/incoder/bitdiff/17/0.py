
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 15 bit positions.
    """
    if a == b:
        return False
    bit_diff = a ^ b
    bit_diff = (bit_diff >> 1) & 0x55555555
    bit_diff = (bit_diff << 2) & 0x33333333
    bit_diff = (bit_diff >> 2) & 0x00ff00ff
    bit_diff = (bit_diff << 4) & 0x0000ffff
    return bit_diff == 0


def bit_diffs(a, b):
    """
    Returns the number of bit differences between the two numbers.
    """
    if a == b:
        return 0
    bit_diff = a ^ b
    bit_diff = (bit_diff >> 1) & 0x55555555
    bit_diff = (bit_diff << 2) & 0x33333333
    bit_diff = (bit_diff >> 2) & 0x00ff00ff
    bit_diff = (bit_diff << 4) & 0x0000ffff
    return bit_diff


def bit_diffs_mod(a, b):
    """
    Returns the number of bit differences between the two numbers, modulo 256.
    """
    if a == b:
        return 0
    bit_diff = a ^ b
    bit_diff = (bit_diff >> 1) & 0x55555555
    bit_diff = (bit_diff << 2) & 0x33333333
    bit_diff = (bit_diff >> 2) & 0x00ff00ff
    bit_diff = (bit_diff << 4) & 0x0000ffff
    return bit_diff % 256


def bit_diffs_mod_2(a, b):
    """
    Returns the number of bit differences between the two numbers, modulo 256.
    """
    if a == b:
        return 0
    bit_diff = a ^ b
    bit_diff = (bit_diff >> 1) & 0x55555555
    bit_diff = (bit_diff << 2) & 0x33333333
    bit_diff = (bit_diff >> 2) & 0x00ff00ff
    bit_diff = (bit_diff << 4) & 0x0000ffff
    return bit_diff % 256


def bit_diffs_mod_3(a, b):
    """
    Returns the number of bit differences between the two numbers, modulo 256.
    """
    if a == b:
        return 0
    bit_diff = a ^ b
    bit_diff = (bit_diff >> 1) & 0x55555555
    bit_diff = (bit_diff << 2) & 0x33333333
    bit_diff = (bit_diff >> 2) & 0x00ff00ff
    bit_diff = (bit_diff << 4) & 0x0000ffff
    return bit_diff % 256


def bit_diffs_mod_4(a, b):
    """
    Returns the number of bit differences between the two numbers, modulo 256.
    """
    if a == b:
        return 0
    bit_diff = a ^ b
    bit_diff = (bit_diff >> 1) & 0x55555555
    bit_diff = (bit_diff << 2) & 0x33333333
    bit_diff = (bit_diff >> 2) & 0x