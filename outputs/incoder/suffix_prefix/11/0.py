
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('12345678')
    ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678']
    """
    prefixes = []
    for length in range(len(string) + 1):
        prefixes.append(string[:length])
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('12345678')
    ['7', '78', '789', '7898', '78987', '789876', '7898765', '78987654', '789876543', '7898765432', '78987654321', '789876543210']
    """
    suffixes = []
    for length in range(len(string) + 1):
        suffixes.append(string[-length:])
    return suffixes


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
    substrings = []
    for length in range(len(string) + 1):
        substrings.append(string[length:])
    return substrings


def all_substrings_with_replacements(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_with_replacements('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
    substrings = []
    for length in range(len(string) + 1):
        substrings.append(string[:length])
    return substrings


def all_substrings_with_complements(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_with_complements('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
    substrings = []
    for length in range(len(string) + 1):
        substrings.append(string[length::-1])
    return substrings


def all_substrings_with_complements_and_replacements(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_with_complements_and_replacements('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1', '1234567', '123456', '12345', '1234', '123', '12', '1', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
    substrings = []
    for length in range(len(string) + 1):
        substrings.append(string[:length])