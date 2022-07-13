
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('abc')
    ['abc', 'ab', 'a']
    """

def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('abc')
    ['abc', 'ab', 'a']
    """

def all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix('abc', 'abc')
    ['abc', 'ab', 'a']
    """

def all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix('abc', 'abc')
    ['abc', 'ab', 'a']
    """

def all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix_and_suffix('abc', 'abc', 'abc')
    ['abc', 'ab', 'a']
    """

def all_suffixes_with_suffix_and_prefix(string: str, suffix: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix_and_prefix('abc', 'abc', 'abc')
    ['abc', 'ab', 'a']
    """

def all_suffixes_with_suffix_and_prefix_and_suffix(string: str, suffix: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix_and_prefix_and_suffix('abc', 'abc', 'abc')
    ['abc', 'ab', 'a']
    """

def all_suffixes_with_suffix_and_prefix_and_suffix_and_prefix(string