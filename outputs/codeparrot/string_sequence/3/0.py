def string_sequence(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(1)
    '0, 1'
    """
    return str(n) + ',' + str(n + 1)


def string_to_number(s: str) -> int:
    """ Return a string containing a number from a string.
    >>> string_to_number('0, 1')
    '0'
    """
    return int(s)


def string_to_number_list(s: str) -> list:
    """ Return a list containing a number from a string.
    >>> string_to_number_list('0, 1')
    ['0', '1']
    """
    return [int(s) for s in s.split(',')]


def string_to_number_dict(s: str) -> dict:
    """ Return a dict containing a number from a string.
    >>> string_to_number_dict('0, 1')
    {'0': 0, '1': 1}
    """
    return dict(zip(string_to_number(s.split(',')), string_to_number(s.split(',')))


def string_to_number_list_dict(s: str) -> dict:
    """ Return a dict containing a number from a string.
    >>> string_to_number_list_dict('0, 1')
    {'0': 0, '1': 1}
    """
    return dict(zip(string_to_number_list(s.split(',')), string_to_number_list(s.split(',')))


def string_to_number_dict_list(s: str) -> list:
    """ Return a list containing a number from a string.
    >>> string_to_number_dict_list('0, 1')
    ['0', '1']
    """
    return [int(s) for s in s.split(',')]


def string_to_number_list_list(s: str) -> list:
    """ Return a list containing a number from a string.
    >>> string_to_number_list_list('0, 1')
    ['0', '1']
    """
    return [int(s) for s in s.split(',')]


def string_to_number_dict_list