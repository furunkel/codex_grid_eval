
def string_sequence(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0	1'
    """
    return f'0\t{n}'


@given(st.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_with_n_as_a_parameter(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0	1'
    """
    return f'0\t{n}'


@given(st.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_with_n_as_a_parameter_and_a_default_value_of_1(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0	1'
    """
    return f'0\t{n}'


@given(st.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_with_n_as_a_parameter_and_a_default_value_of_2(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0	1'
    """
    return f'0\t{n}'


@given(st.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_with_n_as_a_parameter_and_a_default_value_of_3(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0	1'
    """
    return f'0\t{n}'


@given(st.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_with_n_as_a_parameter_and_a_default_value_of_4(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0	1'
    """
    return f'0\t{n}'


@given(st.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_with_n_as_a_parameter_and_a_default_value_of_5(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0	1'
    """
    return f'0\t{n}'


@given(st.integers(min_value=0))
@settings(deadline=None)
def test_string_sequence_with_n_as_a_parameter_and_a_default_value_of_6(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0	1'
    """
    return f'0\t{n}'


@given(st.integers(