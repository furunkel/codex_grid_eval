
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly fifteen bit positions.
    """
    bit_diff = 0
    for bit_idx in range(16):
        if (a[bit_idx] != b[bit_idx]) and (a[bit_idx] & 1):
            bit_diff += 1
    return bit_diff


def bit_diff2(a, b):
    """
    Returns whether the two numbers differ at exactly eight bit positions.
    """
    bit_diff = 0
    for bit_idx in range(8):
        if (a[bit_idx] != b[bit_idx]) and (a[bit_idx] & 1):
            bit_diff += 1
    return bit_diff


def bit_diff3(a, b):
    """
    Returns whether the two numbers differ at exactly four bit positions.
    """
    bit_diff = 0
    for bit_idx in range(4):
        if (a[bit_idx] != b[bit_idx]) and (a[bit_idx] & 1):
            bit_diff += 1
    return bit_diff


def bit_diff4(a, b):
    """
    Returns whether the two numbers differ at exactly two bit positions.
    """
    bit_diff = 0
    for bit_idx in range(2):
        if (a[bit_idx] != b[bit_idx]) and (a[bit_idx] & 1):
            bit_diff += 1
    return bit_diff


def bit_diff5(a, b):
    """
    Returns whether the two numbers differ at exactly one bit position.
    """
    bit_diff = 0
    if a[15] != b[15] and a[15] & 1:
        bit_diff += 1
    return bit_diff


def bit_diff6(a, b):
    """
    Returns whether the two numbers differ at exactly zero bit positions.
    """
    bit_diff = 0
    if a[15] != b[15] and not a[15] & 1:
        bit_diff += 1
    return bit_diff


def bit_diff7(a, b):
    """
    Returns whether the two numbers differ at exactly one bit position.
    """
    bit_diff = 0
    if a[7] != b[7] and a[7] & 1:
        bit_diff += 1
    return bit_diff


def bit_diff8(a, b):
    """
    Returns whether the two numbers differ at exactly two bit positions.
    """
    bit_diff = 0
    if a[7] != b[7] and a[7] & 1:
        bit_diff += 1
    return bit_diff


def bit_diff9(a, b):
    """
    Returns whether the two numbers differ at exactly four bit positions.
    """
    bit_diff = 0
    if a[7] != b[7] and a[7] & 1:
        bit_diff += 1
    return bit_diff


def bit_diff10(a, b):
    """
    Returns whether the two numbers differ at exactly eight bit positions.
    """
    bit_diff = 0
    if a[7] != b[7] and a[