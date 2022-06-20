
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
    return [string[:i] for i in range(len(string), 0, -1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
    return [string[i:] for i in range(len(string), 0, -1)]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8', '1234567', '234567', '34567', '4567', '567', '67', '7', '123456', '23456', '3456', '456', '56', '6', '12345', '2345', '345', '45', '5', '1234', '234', '34', '4', '123', '23', '3', '12', '2', '1']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_substrings_with_length(string: str, length: int) -> List[str]:
    """ Return list of all substrings of length `length` from longest to shortest of the input string
    >>> all_substrings_with_length('12345678', 3)
    ['123', '234', '345', '456', '567', '678']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1)]


def all_substrings_with_length_and_offset(string: str, length: int, offset: int) -> List[str]:
    """ Return list of all substrings of length `length` from longest to shortest of the input