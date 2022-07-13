
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
#    print(string)
    prefixes = []
    for i in range(len(string) - 1):
        if string[i] == ' ':
            prefixes.append(string[i + 1:])
        else:
            prefixes.append(string[i:i + 2])
    return prefixes


def get_prefix_length(string: str) -> int:
    """ Return the length of the longest prefix string
    >>> get_prefix_length('12345678')
    4
    """
    prefixes = all_prefixes(string)
    return len(prefixes)


def get_prefix_length_from_string(string: str) -> int:
    """ Return the length of the longest prefix string
    >>> get_prefix_length_from_string('12345678')
    4
    """
    prefixes = all_prefixes(string)
    return len(prefixes)


def get_prefix_length_from_list(string: str) -> int:
    """ Return the length of the longest prefix string
    >>> get_prefix_length_from_list('12345678')
    4
    """
    prefixes = all_prefixes(string)
    return len(prefixes)


def get_prefix_length_from_list_from_string(string: str) -> int:
    """ Return the length of the longest prefix string
    >>> get_prefix_length_from_list_from_string('12345678')
    4
    """
    prefixes = all_prefixes(string)
    return len(prefixes)


def get_prefix_length_from_list_from_string_from_list(string: str) -> int:
    """ Return the length of the longest prefix string
    >>> get_prefix_length_from_list_from_string_from_list('12345678')
    4
    """
    prefixes = all_prefixes(string)
    return len(prefixes)


def get_prefix_length_from_list_from_string_from_list(string: str) -> int:
    """ Return the length of the longest prefix string
    >>> get_prefix_length_from_list_from_string