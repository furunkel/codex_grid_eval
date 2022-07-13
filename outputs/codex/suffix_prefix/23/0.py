
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('12345678')
    ['8', '78', '678', '5678', '45678', '345678', '2345678', '12345678']
    """
    return [string[i:] for i in range(len(string))]


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('12345678')
    ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('12345678')
    ['1', '2', '3', '4', '5', '6', '7', '8', '12', '23', '34', '45', '56', '67', '78', '123', '234', '345', '456', '567', '678', '1234', '2345', '3456', '4567', '5678', '12345', '23456', '34567', '45678', '123456', '234567', '345678', '1234567', '2345678', '12345678']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_substrings_with_length(string: str, length: int) -> List[str]:
    """ Return list of all substrings of length from shortest to longest of the input string
    >>> all_substrings_with_length('12345678', 3)
    ['123', '234', '345', '456', '567', '678']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1)]


def all_substrings_with_length_and_offset(string: str, length: int, offset: int) -> List[str]:
    """ Return list of all substrings of length from shortest to longest of the input string
    >>> all_substrings_with_length