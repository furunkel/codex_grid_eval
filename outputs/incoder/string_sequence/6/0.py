
def string_sequence(n: int) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0; 1'
    """
    return ';'.join(str(i) for i in range(n))


@njit
def string_sequence_with_prefix(n: int, prefix: str) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_prefix(1, '0')
    '0; 1'
    """
    return prefix + ';'.join(str(i) for i in range(n))


@njit
def string_sequence_with_prefix_and_suffix(n: int, prefix: str, suffix: str) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_prefix_and_suffix(1, '0', '1')
    '0; 1; 2'
    """
    return prefix + ';'.join(str(i) for i in range(n)) + suffix


@njit
def string_sequence_with_prefix_and_suffix_and_separator(n: int, prefix: str, suffix: str, separator: str) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_prefix_and_suffix_and_separator(1, '0', '1', ';')
    '0; 1; 2'
    """
    return prefix + ';'.join(str(i) for i in range(n)) + separator + suffix


@njit
def string_sequence_with_prefix_and_suffix_and_separator_at_end(n: int, prefix: str, suffix: str, separator: str) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_prefix_and_suffix_and_separator_at_end(1, '0', '1', ';')
    '0; 1; 2'
    """
    return prefix + ';'.join(str(i) for i in range(n)) + separator + suffix


@njit
def string_sequence_with_prefix_and_suffix_and_separator_at_end_and_separator(n: int, prefix: str, suffix: str, separator: str) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_prefix_and_suffix_and_separator_at_end_and_separator(1, '0', '1', ';')
    '0; 1; 2'
    """
    return prefix + ';'.join(str(i) for i in range(n)) + separator + suffix


@njit
def string_sequence_with_prefix_and_suffix_and_separator_at_end_and_separator_at_end(n: int, prefix: str, suffix: str, separator: str) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_prefix_and_suffix_and_separator_at_end_and_separator_at_end(1, '0', '1', ';')
    '0; 1; 2'
    """
    return prefix + ';'.join(str(i) for i in range(n)) + separator + suffix


@njit
def string_sequence_with_prefix_and_suffix_and_separator_at_end_and_separator_at_end_and_separator(n: int, prefix: str, suffix: str, separator: str) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 