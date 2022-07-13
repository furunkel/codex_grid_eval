
def string_sequence(n: int) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0#1'
    """
    return f'0#{n}'


@njit
def string_sequence_with_prefix(n: int, prefix: str) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_prefix(1, '0#')
    '0#1'
    """
    return f'{prefix}{n}'


@njit
def string_sequence_with_prefix_and_suffix(n: int, prefix: str, suffix: str) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_prefix_and_suffix(1, '0#', '1#')
    '0#1#2'
    """
    return f'{prefix}{n}{suffix}'


@njit
def string_sequence_with_prefix_and_suffix_and_delimiter(n: int, prefix: str, suffix: str, delimiter: str) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_prefix_and_suffix_and_delimiter(1, '0#', '1#', '2#')
    '0#1#2#'
    """
    return f'{prefix}{n}{suffix}{delimiter}'


@njit
def string_sequence_with_prefix_and_suffix_and_delimiter_and_delimiters(
        n: int, prefix: str, suffix: str, delimiter: str, delimiters: str
) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_prefix_and_suffix_and_delimiter_and_delimiters(1, '0#', '1#', '2#', '3#')
    '0#1#2#3#'
    """
    return f'{prefix}{n}{suffix}{delimiter}{delimiters}'


@njit
def string_sequence_with_prefix_and_suffix_and_delimiter_and_delimiters_and_delimiters(
        n: int, prefix: str, suffix: str, delimiter: str, delimiters: str, delimiters2: str
) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_prefix_and_suffix_and_delimiter_and_delimiters_and_delimiters(
            1, '0#', '1#', '2#', '3#', '4#')
    '0#1#2#3#4#'
    """
    return f'{prefix}{n}{suffix}{delimiter}{delimiters}{delimiters2}'


@njit
def string_sequence_with_prefix_and_suffix_and_delimiter_and_delimiters_and_delimiters_and_delimiters(
        n: int, prefix: str, suffix: str, delimiter: str, delimiters: str, delimiters2: str, delimiters3: str
) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_prefix_