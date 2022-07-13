
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('suffix')
    ['x', 'ix', 'fix', 'ffix', 'uffix', 'suffix']
    """
    suffixes = []
    for suffix in string.split('-'):
        suffixes.append(suffix)
        suffixes.extend(all_suffixes(suffix))
    return suffixes


def all_prefixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_prefixes('prefix-suffix')
    ['-suffix', '-ix', '-fix', '-f-ix', '-ffix', '-uffix', '-prefix']
    """
    prefixes = []
    for prefix in string.split('-'):
        prefixes.append(prefix)
        prefixes.extend(all_prefixes(prefix))
    return prefixes


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('prefix-suffix')
    ['prefix', 'suffix']
    """
    substrings = []
    for substring in string.split('-'):
        substrings.append(substring)
        substrings.extend(all_substrings(substring))
    return substrings


def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_prefixes('prefix-suffix')
    ['prefix', 'suffix']
    """
    substrings = []
    for substring in string.split('-'):
        substrings.append(substring)
        substrings.extend(all_substrings_prefixes(substring))
    return substrings


def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_suffixes('prefix-suffix')
    ['prefix', 'suffix']
    """
    substrings = []
    for substring in string.split('-'):
        substrings.append(substring)
        substrings.extend(all_substrings_suffixes(substring))
    return substrings


def all_substrings_prefixes_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_prefixes_suffixes('prefix-suffix')
    ['prefix', 'suffix']
    """
    substrings = []
    for substring in string.split('-'):
        substrings.append(substring)
        substrings.extend(all_substrings_prefixes_suffixes(substring))
    return substrings


def all_substrings_suffixes_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_suffixes_prefixes('prefix-suffix')
    ['prefix', 'suffix']
    """
    substrings = []
    for substring in string.split('-'):
        substrings.append(substring)
        substrings.extend(all_