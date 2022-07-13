
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for c in string:
        prefixes.append(c)
        prefixes.extend(all_prefixes(c))
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['', 'c', 'bc', 'abc']
    """
    suffixes = []
    for c in reversed(string):
        suffixes.append(c)
        suffixes.extend(all_suffixes(c))
    return suffixes


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('abc')
    ['', 'a', 'ab', 'abc']
    """
    substrings = []
    for c in string:
        substrings.append(c)
        substrings.extend(all_substrings(c))
    return substrings


def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    that start with the shortest input string
    >>> all_substrings_prefixes('abc')
    ['', 'a', 'ab', 'abc']
    """
    substrings = []
    for c in string:
        substrings.append(c)
        substrings.extend(all_substrings_prefixes(c))
    return substrings


def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    that end with the shortest input string
    >>> all_substrings_suffixes('abc')
    ['', 'a', 'ab', 'abc']
    """
    substrings = []
    for c in reversed(string):
        substrings.append(c)
        substrings.extend(all_substrings_suffixes(c))
    return substrings


def all_substrings_prefixes_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    that start with the shortest input string and end with the longest input string
    >>> all_substrings_prefixes_suffixes('abc')
    ['', 'a', 'ab', 'abc']
    """
    substrings = []
    for c in string:
        substrings.append(c)
        substrings.extend(all_substrings_prefixes_suffixes(c))
    return substrings


def all_substrings_prefixes_suffixes_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    that start with the shortest input string and end with the longest input string
    and end with the shortest input string
    >>> all_substrings_prefixes_suffixes_prefixes('abc')
    ['', 'a', 'ab', 'abc']
    """
    substrings = []
    for c in string:
