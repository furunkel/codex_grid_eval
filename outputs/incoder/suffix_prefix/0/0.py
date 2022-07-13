
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('abc')
    ['abc', 'ab', 'a']
    """
    prefixes = []
    prefix_length = 0
    for c in string:
        if c.isalpha():
            prefix_length += 1
        else:
            prefix_length = 0
        prefixes.append(string[prefix_length:])
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('abc')
    ['', 'c', 'b']
    """
    suffixes = []
    suffix_length = 0
    for c in string:
        if c.isalpha():
            suffix_length += 1
        else:
            suffix_length = 0
        suffixes.append(string[:-suffix_length])
    return suffixes


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings('abc')
    ['abc', 'ab', 'a']
    """
    substrings = []
    substring = ""
    for c in string:
        if c.isalpha():
            substring = substring + c
        else:
            substrings.append(substring)
            substring = ""
    substrings.append(substring)
    return substrings


def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefixes('abc')
    ['abc', 'ab', 'a']
    """
    substrings = []
    substring = ""
    for c in string:
        if c.isalpha():
            substring = substring + c
        else:
            substrings.append(substring)
            substring = ""
    substrings.append(substring)
    return substrings


def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_suffixes('abc')
    ['abc', 'ab', 'a']
    """
    substrings = []
    substring = ""
    for c in string:
        if c.isalpha():
            substring = substring + c
        else:
            substrings.append(substring)
            substring = ""
    substrings.append(substring)
    return substrings


def all_substrings_prefixes_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefixes_suffixes('abc')
    ['abc', 'ab', 'a']
    """
    substrings = []
    substring = ""
    for c in string:
        if c.isalpha():
            substring = substring + c
        else:
            substrings.append(substring)
            substring = ""
    substrings.append(substring)
    return substrings


def all_substrings_length