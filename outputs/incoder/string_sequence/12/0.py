
def string_sequence(n: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0#1'
    """
    return "".join(str(n) for n in range(n))


@njit
def string_sequence_with_zero(n: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_zero(1)
    '0#1'
    """
    return "".join(str(n) for n in range(n)) + "#"


@njit
def string_sequence_with_zero_and_one(n: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_zero_and_one(1)
    '0#1'
    """
    return "".join(str(n) for n in range(n)) + "#0"


@njit
def string_sequence_with_zero_and_one_and_two(n: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_zero_and_one_and_two(1)
    '0#1#2'
    """
    return "".join(str(n) for n in range(n)) + "#0#1"


@njit
def string_sequence_with_zero_and_one_and_two_and_three(n: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_zero_and_one_and_two_and_three(1)
    '0#1#2#3'
    """
    return "".join(str(n) for n in range(n)) + "#0#1#2"


@njit
def string_sequence_with_zero_and_one_and_two_and_three_and_four(n: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_zero_and_one_and_two_and_three_and_four(1)
    '0#1#2#3#4'
    """
    return "".join(str(n) for n in range(n)) + "#0#1#2#3"


@njit
def string_sequence_with_zero_and_one_and_two_and_three_and_four_and_five(n: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_zero_and_one_and_two_and_three_and_four_and_five(1)
    '0#1#2#3#4#5'
    """
    return "".join(str(n) for n in range(n)) + "#0#1#2#3#4"


@njit
def string_sequence_with_zero_and_one_and_two_and_three_and_four_and_five_and_six(n: int) -> str:
    """ Return a string containing number sign-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_with_zero_and_one_and_two_and_three_and_four