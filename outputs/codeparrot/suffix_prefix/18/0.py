
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('prefix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """

def all_suffixes_with_prefix(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix('prefix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """

def all_suffixes_with_suffix(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix('suffix')
    ['suffix', 'refix', 'efix', 'fix', 'ix', 'x']
    """

def all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix_and_suffix('prefix', prefix, suffix)
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """

def all_suffixes_with_suffix_and_prefix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix_and_prefix('suffix', prefix, suffix)
    ['suffix', 'refix', 'efix', 'fix', 'ix', 'x']
    """

def all_suffixes_with_prefix_and_suffix_and_prefix(string: str, prefix: str, suffix: str, prefix_and_suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix_and_suffix('prefix', prefix, suffix, prefix_and_suffix)
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """

def all_suffixes_with_suffix_and_prefix_and_suffix(string: str,