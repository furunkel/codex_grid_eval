
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('prefix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """
    suffixes = []
    for suffix in string.split('-'):
        suffixes.append(suffix)
        suffixes.extend(all_suffixes(suffix))
    return suffixes


def all_prefixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_prefixes('prefix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """
    prefixes = []
    for prefix in string.split('-'):
        prefixes.append(prefix)
        prefixes.extend(all_prefixes(prefix))
    return prefixes


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings('prefix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """
    substrings = []
    for substring in string.split('-'):
        substrings.append(substring)
        substrings.extend(all_substrings(substring))
    return substrings


def all_substrings_without_duplicates(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_without_duplicates('prefix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """
    substrings = []
    for substring in string.split('-'):
        substrings.append(substring)
        substrings.extend(all_substrings_without_duplicates(substring))
    return list(set(substrings))


def all_substrings_with_duplicates(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_with_duplicates('prefix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """
    substrings = []
    for substring in string.split('-'):
        substrings.append(substring)
        substrings.extend(all_substrings_with_duplicates(substring))
    return list(set(substrings))


def all_substrings_without_duplicates_and_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_without_duplicates_and_prefixes('prefix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """
    substrings = []
    for substring in string.split('-'):
        substrings.append(substring)
        substrings.extend(all_substrings_without_duplicates_and_prefixes(substring))
    return list(set(substrings))


def all_substrings_without_duplicates_and_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_without_duplicates_and_suffixes('