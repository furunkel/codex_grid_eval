
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the ', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resu', 'reverse the resul', 'reverse the result', 'reverse the result!', 'reverse the result!!', 'reverse the result!!!']
    """

def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the ', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resul', 'reverse the result', 'reverse the result!', 'reverse the result!!!']
    """

def all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_prefix('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resul', 'reverse the result', 'reverse the result!', 'reverse the result!!!']
    """

def all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_suffix('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resul', 'reverse the result', 'reverse