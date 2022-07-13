
def string_sequence(n: int) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence(1)
    '0'
    """
    return ';'.join(str(i) for i in range(n))


def string_sequence_with_step(n: int, step: int) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n exclusive with a given step.
    >>> string_sequence_with_step(1, 1)
    '0'
    >>> string_sequence_with_step(2, 1)
    '0;1'
    >>> string_sequence_with_step(2, 2)
    '0'
    """
    return ';'.join(str(i) for i in range(0, n, step))


def string_sequence_with_step_and_offset(n: int, step: int, offset: int) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n exclusive with a given step and offset.
    >>> string_sequence_with_step_and_offset(1, 1, 0)
    '0'
    >>> string_sequence_with_step_and_offset(2, 1, 0)
    '0;1'
    >>> string_sequence_with_step_and_offset(2, 2, 0)
    '0'
    >>> string_sequence_with_step_and_offset(2, 1, 1)
    '1'
    """
    return ';'.join(str(i) for i in range(offset, n, step))


def string_sequence_with_step_and_offset_and_length(n: int, step: int, offset: int, length: int) -> str:
    """ Return a string containing semicolon-delimited numbers starting from 0 upto n exclusive with a given step and offset and length.
    >>> string_sequence_with_step_and_offset_and_length(1, 1, 0, 1)
    '0'
    >>> string_sequence_with_step_and_offset_and_length(2, 1, 0, 2)
    '0;1'
    >>> string_sequence_with_step_and_offset_and_length(2, 2, 0, 1)
    '