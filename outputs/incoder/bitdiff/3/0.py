
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 1 bit position.
    """
    return a ^ b


@numba.njit
def bit_flip(a, bit):
    """
    Flips bit at position bit in a.
    """
    return a ^ (1 << bit)


@numba.njit
def bit_flip2(a, bit):
    """
    Flips bit at position bit in a.
    """
    return a ^ ((1 << bit) | (1 << bit))


@numba.njit
def bit_flip3(a, bit):
    """
    Flips bit at position bit in a.
    """
    return a ^ ((1 << bit) | (1 << bit) | (1 << bit))


@numba.njit
def bit_flip4(a, bit):
    """
    Flips bit at position bit in a.
    """
    return a ^ ((1 << bit) | (1 << bit) | (1 << bit) | (1 << bit))


@numba.njit
def bit_flip5(a, bit):
    """
    Flips bit at position bit in a.
    """
    return a ^ ((1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit))


@numba.njit
def bit_flip6(a, bit):
    """
    Flips bit at position bit in a.
    """
    return a ^ ((1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit))


@numba.njit
def bit_flip7(a, bit):
    """
    Flips bit at position bit in a.
    """
    return a ^ ((1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit))


@numba.njit
def bit_flip8(a, bit):
    """
    Flips bit at position bit in a.
    """
    return a ^ ((1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit))


@numba.njit
def bit_flip9(a, bit):
    """
    Flips bit at position bit in a.
    """
    return a ^ ((1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit))


@numba.njit
def bit_flip10(a, bit):
    """
    Flips bit at position bit in a.
    """
    return a ^ ((1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit) | (1 << bit))


@numba.n