
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('prefix')
    ['p', 'pr', 'pre', 'pref', 'prefi', 'prefix']
    """

def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('suffix')
    ['s', 'sh', 'shs', 'shs', 'shs', 'shs', 'shs']
    """

def all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_prefix('suffix', 'prefix')
    ['p', 'pr', 'pre', 'pref', 'pre', 'pref', 'prefi', 'suffix']
    """

def all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_suffix('suffix', 'suffix')
    ['s', 'sh', 'shs', 'shs', 'shs', 'shs', 'shs']
    """

def all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_prefix_and_suffix('suffix', 'prefix', 'suffix')
    ['p', 'pr', 'pre', 'pref', 'pre', 'pref', 'prefi', 'suffix']
    """

def all_suffixes_with_suffix_and_prefix(string: str, suffix: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_suffix_and_prefix('suffix', 'suffix', 'prefix')
    ['p', 'pr', 'pre', 'pref', 'pre', 'pref', 'prefi', 'suffix']
    """

def all_suffixes_with_suffix_and_prefix_and_suffix(string: str, suffix: