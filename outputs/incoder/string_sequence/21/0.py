
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence(1)
    '0'
    """
    return ' '.join(str(i) for i in range(n))


@njit
def string_sequence_with_spaces(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_spaces(1)
    '0 1'
    """
    return ' '.join(str(i) for i in range(n))


@njit
def string_sequence_with_commas(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas(1)
    '0,1'
    """
    return ', '.join(str(i) for i in range(n))


@njit
def string_sequence_with_commas_and_spaces(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas_and_spaces(1)
    '0, 1'
    """
    return ', '.join(str(i) for i in range(n))


@njit
def string_sequence_with_commas_and_spaces_and_zero(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas_and_spaces_and_zero(1)
    '0, 1'
    """
    return ', '.join(str(i) for i in range(n))


@njit
def string_sequence_with_commas_and_spaces_and_zero_and_one(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas_and_spaces_and_zero_and_one(1)
    '0, 1'
    """
    return ', '.join(str(i) for i in range(n))


@njit
def string_sequence_with_commas_and_spaces_and_zero_and_one_and_two(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas_and_spaces_and_zero_and_one_and_two(1)
    '0, 1'
    """
    return ', '.join(str(i) for i in range(n))


@njit
def string_sequence_with_commas_and_spaces_and_zero_and_one_and_two_and_three(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas_and_spaces_and_zero_and_one_and_two_and_three(1)
    '0, 1'
    """
    return ', '.join(str(i) for i in range(n))


@njit
def string_sequence_with_commas_and_spaces_and_zero_and_one_and_two_and_three_and_four(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas_and_spaces_and_zero_and_one_and_two_and_three_and_four(1)
    '0, 1'
    """
    return ', '.join(str(i) for i in range(n))


@njit
def string_sequence_with_commas_and_space