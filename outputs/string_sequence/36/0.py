
def string_sequence(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence(1)
    '0'
    """
    return '\t'.join(str(i) for i in range(n))


def string_sequence_with_newline(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_newline(1)
    '0\\n'
    """
    return '\t'.join(str(i) for i in range(n)) + '\n'


def string_sequence_with_newline_and_tab(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_newline_and_tab(1)
    '0\\t\\n'
    """
    return '\t'.join(str(i) for i in range(n)) + '\t\n'


def string_sequence_with_newline_and_tab_and_space(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_newline_and_tab_and_space(1)
    '0\\t \\n'
    """
    return '\t'.join(str(i) for i in range(n)) + '\t \n'


def string_sequence_with_newline_and_tab_and_space_and_comma(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_newline_and_tab_and_space_and_comma(1)
    '0\\t ,\\n'
    """
    return '\t'.join(str(i) for i in range(n)) + '\t ,\n'


def string_sequence_with_newline_and_tab_and_space_and_comma_and_semicolon(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_newline_and