
def string_sequence(n: int) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence(1)
    '0'
    """
    return ''.join([str(n) for n in range(n)])


@njit
def string_sequence_with_prefix(n: int, prefix: str) -> List[str]:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix(3, '0')
    ['0', '1', '2']
    """
    strings = []
    for i in range(n):
        strings.append(prefix + str(i))
    return strings


@njit
def string_sequence_with_prefix_and_suffix(n: int, prefix: str, suffix: str) -> List[str]:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix_and_suffix(3, '0', '1')
    ['0', '1', '2']
    """
    strings = []
    for i in range(n):
        strings.append(prefix + str(i) + suffix)
    return strings


@njit
def string_sequence_with_prefix_and_suffix_and_separator(n: int, prefix: str, suffix: str, separator: str) -> List[str]:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix_and_suffix_and_separator(3, '0', '1', '-')
    ['0-1', '0-2', '0-3']
    """
    strings = []
    for i in range(n):
        strings.append(prefix + str(i) + suffix + separator)
    return strings


@njit
def string_sequence_with_prefix_and_suffix_and_separator_at_end(n: int, prefix: str, suffix: str, separator: str) -> List[str]:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix_and_suffix_and_separator_at_end(3, '0', '1', '-')
    ['0-1', '0-2', '0-3']
    """
    strings = []
    for i in range(n):
        strings.append(prefix + str(i) + suffix + separator)
    return strings


@njit
def string_sequence_with_prefix_and_suffix_and_separator_at_end_and_separator(n: int, prefix: str, suffix: str, separator: str) -> List[str]:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix_and_suffix_and_separator_at_end_and_separator(3, '0', '1', '-', ':')
    ['0-1:', '0-2:', '0-3']
    """
    strings = []
    for i in range(n):
        strings.append(prefix + str(i) + suffix + separator + separator)
    return strings


@njit
def string_sequence_with_prefix_and_suffix_and_separator_at_end_and_separator_at_end(n: int, prefix: str, suffix: str, separator: str, separator2: str) -> List[str]:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix_and_suffix_and_separator_at_end_and_separator_