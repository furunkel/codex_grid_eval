
def string_sequence(n: int) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence(1)
    '0'
    """
    return ';'.join(str(i) for i in range(n))


@njit
def string_sequence_with_separator(n: int, separator: str = ';') -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_separator(1)
    '0;1'
    """
    return separator.join(str(i) for i in range(n))


@njit
def string_sequence_with_separator_at_end(n: int, separator: str = ';') -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_separator_at_end(1)
    '0;1'
    """
    return separator.join(str(i) for i in range(n)) + separator


@njit
def string_sequence_with_separator_at_begin(n: int, separator: str = ';') -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_separator_at_begin(1)
    '1;0'
    """
    return separator.join(str(i) for i in range(n)) + separator


@njit
def string_sequence_with_separator_at_beginning_and_end(n: int, separator: str = ';') -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_separator_at_beginning_and_end(1)
    '1;0'
    """
    return separator.join(str(i) for i in range(n)) + separator


@njit
def string_sequence_with_separator_at_beginning_and_end_and_middle(n: int, separator: str = ';') -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_separator_at_beginning_and_end_and_middle(1)
    '1;0;2'
    """
    return separator.join(str(i) for i in range(n)) + separator


@njit
def string_sequence_with_separator_at_beginning_and_end_and_middle_and_middle(n: int, separator: str = ';') -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_separator_at_beginning_and_end_and_middle_and_middle(1)
    '1;0;2;3'
    """
    return separator.join(str(i) for i in range(n)) + separator


@njit
def string_sequence_with_separator_at_beginning_and_end_and_middle_and_middle_and_middle(n: int, separator: str = ';') -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_separator_at_beginning_and_end_and_middle_and_middle_and_middle(1)
    '1;0;2;3;4'
    """
    return separator.join(str(i) for i in range(n)) + separator


@njit