
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
    return [string[i:] for i in range(len(string))]


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
    return [string[:i] for i in range(len(string), 0, -1)]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings of the input string
    >>> all_substrings('12345678')
    ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678', '2', '23', '234', '2345', '23456', '234567', '2345678', '3', '34', '345', '3456', '34567', '345678', '4', '45', '456', '4567', '45678', '5', '56', '567', '5678', '6', '67', '678', '7', '78', '8']
    """
    return all_prefixes(string) + all_suffixes(string)


def all_substrings_of_length(string: str, length: int) -> List[str]:
    """ Return list of all substrings of the input string of the given length
    >>> all_substrings_of_length('12345678', 3)
    ['123', '234', '345', '456', '567', '678']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1)]


def all_substrings_of_length_at_least(string: str, length: int) -> List[str]:
    """ Return list of all substrings of the input string of the given length or longer
    >>> all_substrings_of_length_at_least('12345678', 3)
    ['123', '234', '345', '456