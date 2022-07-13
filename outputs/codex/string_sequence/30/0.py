
def string_sequence(n: int) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence(1)
    '0'
    """
    return '#'.join(str(i) for i in range(n))


def string_sequence_with_spaces(n: int) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_spaces(1)
    '0'
    """
    return '# '.join(str(i) for i in range(n))


def string_sequence_with_spaces_and_newlines(n: int) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_spaces_and_newlines(1)
    '0'
    """
    return '#\n'.join(str(i) for i in range(n))


def string_sequence_with_spaces_and_newlines_and_tabs(n: int) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_spaces_and_newlines_and_tabs(1)
    '0'
    """
    return '#\n\t'.join(str(i) for i in range(n))


def string_sequence_with_spaces_and_newlines_and_tabs_and_carriage_returns(n: int) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_spaces_and_newlines_and_tabs_and_carriage_returns(1)
    '0'
    """
    return '#\n\t\r'.join(str(i) for i in range(n))


def string_sequence_with_spaces_and_newlines_and_tabs_and_carriage_returns_and_form_feeds(n: int) -> str:
    """ Return a string containing hash-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_spaces_and_newlines_and_tabs_and_carriage