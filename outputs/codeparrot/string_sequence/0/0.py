def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0 1'
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


def random_string(length: int) -> str:
    """ Return a random string of length length.
    >>> random_string(10)
    'a'
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def random_string_with_symbols(length: int) -> str:
    """ Return a random string of length length with symbols.
    >>> random_string_with_symbols(10)
    'a'
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def random_string_with_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_and_symbols_