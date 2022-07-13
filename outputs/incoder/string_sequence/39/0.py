
def string_sequence(n: int) -> str:
    """ Return a string containing vertical line-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence(1)
    '0'
    """
    return "".join(str(i) for i in range(n))


def string_sequence_with_prefix(n: int, prefix: str) -> str:
    """ Return a string containing vertical line-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix(1, "0")
    '1'
    """
    return prefix + string_sequence(n)


def string_sequence_with_prefix_and_suffix(n: int, prefix: str, suffix: str) -> str:
    """ Return a string containing vertical line-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix_and_suffix(1, "0", "1")
    '10'
    """
    return prefix + string_sequence(n) + suffix


def string_sequence_with_prefix_and_suffix_and_padding(n: int, prefix: str, suffix: str, padding: str) -> str:
    """ Return a string containing vertical line-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix_and_suffix_and_padding(1, "0", "1", "0")
    '101'
    """
    return prefix + string_sequence(n) + suffix + padding


def string_sequence_with_prefix_and_suffix_and_padding_and_padding(n: int, prefix: str, suffix: str, padding: str, padding_2: str) -> str:
    """ Return a string containing vertical line-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix_and_suffix_and_padding_and_padding(1, "0", "1", "0", "0")
    '10100'
    """
    return prefix + string_sequence(n) + suffix + padding + padding_2


def string_sequence_with_prefix_and_suffix_and_padding_and_padding_2(n: int, prefix: str, suffix: str, padding: str, padding_2: str, padding_3: str) -> str:
    """ Return a string containing vertical line-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix_and_suffix_and_padding_and_padding_2(1, "0", "1", "0", "0", "0")
    '101000'
    """
    return prefix + string_sequence(n) + suffix + padding + padding_2 + padding_3


def string_sequence_with_prefix_and_suffix_and_padding_and_padding_3(n: int, prefix: str, suffix: str, padding: str, padding_2: str, padding_3: str, padding_4: str) -> str:
    """ Return a string containing vertical line-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix_and_suffix_and_padding_and_padding_3(1, "0", "1", "0", "0", "0", "0")
    '1010000'
    """
    return prefix + string_sequence(n) + suffix + padding + padding_2 + padding_3 + padding_4


def string_sequence_with_prefix_and_suffix_and_padding_and_padding_4(n: int, prefix: str, suffix: str, padding: str, padding_2: str, padding_3: str, padding_4: str, padding_5: str) -> str:
    """ Return a string containing vertical line-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_prefix_and_suffix_and_padding_and_padding_4(1, 