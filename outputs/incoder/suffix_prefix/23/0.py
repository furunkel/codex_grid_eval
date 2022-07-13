
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('12345678')
    ['8', '78', '678', '5678', '45678', '345678', '2345678', '12345678']
    """
    suffixes = []
    length = len(string)
    for index in range(length):
        suffixes.append(string[index:])
    return suffixes


@timeit
def all_prefixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_prefixes('12345678')
    ['8', '78', '678', '5678', '45678', '345678', '2345678', '12345678']
    """
    prefixes = []
    length = len(string)
    for index in range(length):
        prefixes.append(string[:index])
    return prefixes


@timeit
def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
    substrings = []
    length = len(string)
    for index in range(length):
        substrings.append(string[index:index+1])
    return substrings


@timeit
def all_substrings_without_repeats(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_without_repeats('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
    substrings = []
    length = len(string)
    for index in range(length):
        substrings.append(string[index:index+1])
    return substrings


@timeit
def all_substrings_without_repeats_without_duplicates(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_without_repeats_without_duplicates('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
    substrings = []
    length = len(string)
    for index in range(length):
        substrings.append(string[index:index+1])
    return substrings


@timeit
def all_substrings_without_repeats_without_duplicates_without_duplicates(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_without_repeats_without_duplicates_without_duplicates('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
    substrings = []
    length = len(string)
    for index in range(length):
        substrings.append(string[index:index+1])
    return substrings


@timeit
def all_substrings_