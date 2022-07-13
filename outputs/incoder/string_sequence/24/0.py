
def string_sequence(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence(1)
    '0'
    """
    return ",".join(str(i) for i in range(n))


@curry
def string_sequence_with_commas(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas(1)
    '0,1'
    """
    return ",".join(str(i) for i in range(n)).split(",")


@curry
def string_sequence_with_commas_with_commas(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas_with_commas(1)
    '0,1,2,3,4,5,6,7,8,9'
    """
    return ",".join(str(i) for i in range(n)).split(",")


@curry
def string_sequence_with_commas_with_commas_with_commas(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas_with_commas_with_commas(1)
    '0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9'
    """
    return ",".join(str(i) for i in range(n)).split(",")


@curry
def string_sequence_with_commas_with_commas_with_commas_with_commas(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas_with_commas_with_commas_with_commas(1)
    '0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9'
    """
    return ",".join(str(i) for i in range(n)).split(",")


@curry
def string_sequence_with_commas_with_commas_with_commas_with_commas_with_commas(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas_with_commas_with_commas_with_commas_with_commas(1)
    '0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9'
    """
    return ",".join(str(i) for i in range(n)).split(",")


@curry
def string_sequence_with_commas_with_commas_with_commas_with_commas_with_commas_with_commas(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_commas_with_commas_with_commas_with_commas_with_commas_with_commas(1)
    '0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,