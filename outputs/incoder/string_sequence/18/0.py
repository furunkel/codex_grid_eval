
def string_sequence(n: int) -> str:
    """ Return a string containing vertical line-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0|1'
    """
    return f'0|{n}'


@given(strategies.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_of_length(n: int) -> None:
    """ Test that string_sequence returns a string containing vertical line-delimited numbers starting from 0 upto n inclusive.
    >>> test_string_sequence_of_length(10)
    """
    assert string_sequence(n) == f'0|{n}'


@given(strategies.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_of_length_with_max_value(n: int) -> None:
    """ Test that string_sequence returns a string containing vertical line-delimited numbers starting from 0 upto n inclusive.
    >>> test_string_sequence_of_length_with_max_value(10)
    """
    assert string_sequence(n) == f'0|{n}'


@given(strategies.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_of_length_with_min_value(n: int) -> None:
    """ Test that string_sequence returns a string containing vertical line-delimited numbers starting from 0 upto n inclusive.
    >>> test_string_sequence_of_length_with_min_value(10)
    """
    assert string_sequence(n) == f'0|{n}'


@given(strategies.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_of_length_with_max_value_and_min_value(n: int) -> None:
    """ Test that string_sequence returns a string containing vertical line-delimited numbers starting from 0 upto n inclusive.
    >>> test_string_sequence_of_length_with_max_value_and_min_value(10)
    """
    assert string_sequence(n) == f'0|{n}'


@given(strategies.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_of_length_with_max_value_and_min_value_with_max_value(n: int) -> None:
    """ Test that string_sequence returns a string containing vertical line-delimited numbers starting from 0 upto n inclusive.
    >>> test_string_sequence_of_length_with_max_value_and_min_value_with_max_value(10)
    """
    assert string_sequence(n) == f'0|{n}'


@given(strategies.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_of_length_with_max_value_and_min_value_with_min_value(n: int) -> None:
    """ Test that string_sequence returns a string containing vertical line-delimited numbers starting from 0 upto n inclusive.
    >>> test_string_sequence_of_length_with_max_value_and_min_value_with_min_value(10)
    """
    assert string_sequence(n) == f'0|{n}'


@given(strategies.integers(min_value=0))
@settings(deadline=None)
