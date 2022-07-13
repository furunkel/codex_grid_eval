
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('prefix')
    ['x', 'ix', 'fix', 'efix', 'refix', 'prefix']
    """

def all_suffixes_with_prefix(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes_with_prefix('prefix')
    ['x', 'ix', 'fix', 'efix', 'prefix']
    """

def all_suffixes_with_suffix(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_suffix('suffix')
    ['x', 'ix', 'fix', 'efix', 'prefix']
    """

def all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_prefix_and_suffix('prefix', prefix, suffix)
    ['x', 'ix', 'fix', 'efix', 'prefix', 'suffix']
    """

def all_suffixes_with_suffix_and_prefix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_suffix_and_prefix('suffix', prefix, suffix)
    ['x', 'ix', 'fix', 'efix', 'prefix', 'suffix']
    """

def all_suffixes_with_prefix_and_suffix_and_prefix(string: str, prefix: str, suffix: str, prefix_suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_prefix_and_suffix_and_prefix('prefix', prefix, suffix, prefix_suffix)
    ['x', 'ix', 'fix', 'efix', 'prefix', 'suffix', 'prefix_suffix']
    """

def all_suffixes_with_suffix_and_prefix_and_suffix(string: str, prefix: str, suffix: