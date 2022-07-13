
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('12345678')
    ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678']
    """

def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('12345678')
    ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678']
    """

def all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_prefix('12345678', prefix='12345678')
    ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678']
    """

def all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_suffix('12345678', suffix='12345678')
    ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678']
    """

def all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_prefix_and_suffix('12345678', prefix='12345678', suffix='12345678')
    ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678']
    """

def all_suffixes_with_suffix_and_prefix(string: str, suffix: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_suffix_and_prefix('12345678', suffix='12345678', prefix='12345678')
    ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678']
    """

def all_suffixes_with_prefix_and_suffix_and_prefix(string: