
def string_sequence(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0, 1'
    """
    return ", ".join(map(str, range(n)))


@njit
def string_sequence_with_commas(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_commas(5)
    '0, 1, 2, 3, 4'
    """
    return ", ".join(map(str, range(n)))


@njit
def string_sequence_with_commas_with_spaces(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_commas_with_spaces(5)
    '0, 1, 2, 3, 4'
    """
    return ", ".join(map(str, range(n))) + " , "


@njit
def string_sequence_with_commas_with_spaces_after_last(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_commas_with_spaces_after_last(5)
    '0, 1, 2, 3, 4'
    """
    return ", ".join(map(str, range(n))) + " , "


@njit
def string_sequence_with_commas_with_spaces_after_last_with_spaces(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_commas_with_spaces_after_last_with_spaces(5)
    '0, 1, 2, 3, 4'
    """
    return ", ".join(map(str, range(n))) + " , "


@njit
def string_sequence_with_commas_with_spaces_after_last_with_spaces_after_last(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_commas_with_spaces_after_last_with_spaces_after_last(5)
    '0, 1, 2, 3, 4'
    """
    return ", ".join(map(str, range(n))) + " , "


@njit
def string_sequence_with_commas_with_spaces_after_last_with_spaces_after_last_with_spaces(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_commas_with_spaces_after_last_with_spaces_after_last_with_spaces(5)
    '0, 1, 2, 3, 4'
    """
    return ", ".join(map(str, range(n))) + " , "


@njit
def string_sequence_with_commas_with_spaces_after_last_with_spaces_after_last_with_spaces_after_last(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_commas_with_spaces_after_last_with_spaces_after_last_with_spaces_after_last(5)
    '0, 1, 2, 3, 4'
    """
    return ", ".join(map(str, range(n))) + " , "


@njit
def string_sequence_with_commas_with_space