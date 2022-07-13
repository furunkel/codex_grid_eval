
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    """
    return [string[i:] for i in range(len(string))]


def longest_common_prefix(string1: str, string2: str) -> str:
    """ Return the longest common prefix of the two input strings
    >>> longest_common_prefix('abc', 'abd')
    'ab'
    """
    for prefix in all_prefixes(string1):
        if prefix in all_suffixes(string2):
            return prefix
    return ''


def longest_common_suffix(string1: str, string2: str) -> str:
    """ Return the longest common suffix of the two input strings
    >>> longest_common_suffix('abc', 'abd')
    'b'
    """
    for suffix in all_suffixes(string1):
        if suffix in all_prefixes(string2):
            return suffix
    return ''


def longest_common_substring(string1: str, string2: str) -> str:
    """ Return the longest common substring of the two input strings
    >>> longest_common_substring('abc', 'abd')
    'ab'
    """
    for prefix in all_prefixes(string1):
        if prefix in all_suffixes(string2):
            return prefix
    return ''


def longest_common_subsequence(string1: str, string2: str) -> str:
    """ Return the longest common subsequence of the two input strings
    >>> longest_common_subsequence('abc', 'abd')
    'ab'
    """
    if not string1 or not string2:
        return ''
    elif string1[0] == string2[0]:
        return string1[0] + longest_common_subsequence(string1[1:], string2[1:])
    else:
        return max