
def string_sequence(n: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence(1)
    '0'
    """
    return "".join(str(n) for n in range(n))


@njit
def string_sequence_with_zero(n: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_zero(1)
    '00'
    """
    return "".join(str(n) for n in range(n)) + "0"


@njit
def string_sequence_with_zero_padding(n: int, padding: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_zero_padding(1, 4)
    '001'
    """
    return "".join(str(n) for n in range(n)) + str(padding)


@njit
def string_sequence_with_zero_padding_with_zero(n: int, padding: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_zero_padding_with_zero(1, 4)
    '001'
    """
    return "".join(str(n) for n in range(n)) + str(padding) + "0"


@njit
def string_sequence_with_zero_padding_with_zero_padding(n: int, padding: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_zero_padding_with_zero_padding(1, 4)
    '001'
    """
    return "".join(str(n) for n in range(n)) + str(padding) + str(padding)


@njit
def string_sequence_with_zero_padding_with_zero_padding_with_zero(n: int, padding: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_zero_padding_with_zero_padding_with_zero(1, 4)
    '001'
    """
    return "".join(str(n) for n in range(n)) + str(padding) + str(padding) + str(padding)


@njit
def string_sequence_with_zero_padding_with_zero_padding_with_zero_padding(n: int, padding: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_zero_padding_with_zero_padding_with_zero_padding(1, 4)
    '001'
    """
    return "".join(str(n) for n in range(n)) + str(padding) + str(padding) + str(padding) + str(padding)


@njit
def string_sequence_with_zero_padding_with_zero_padding_with_zero_padding_with_zero(n: int, padding: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_zero_padding_with_zero_padding_with_zero_padding_with_zero(1, 4)
    '001'
    """
    return "".join(str(n) for n in range(n)) + str(padding) + str(padding) + str(padding) + str(padding) + str(padding