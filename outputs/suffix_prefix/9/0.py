
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the ', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resu', 'reverse the resul', 'reverse the result', 'reverse the result!', 'reverse the result!!', 'reverse the result!!!']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('reverse the result!!!')
    ['!!!', '!!', '!', 't', 'lt!!!', 'lt!!', 'lt!', 'lt', 'esult!!!', 'esult!!', 'esult!', 'esult', 'result!!!', 'result!!', 'result!', 'result', 'ult!!!', 'ult!!', 'ult!', 'ult', 'sult!!!', 'sult!!', 'sult!', 'sult', 'esult!!!', 'esult!!', 'esult!', 'esult', 'result!!!', 'result!!', 'result!', 'result', 't!!!', 't!!', 't!', 't', 'e!!!', 'e!!', 'e!', 'e', 'he result!!!', 'he result!!', 'he result!', 'he result', 'the result!!!', 'the result!!', 'the result!', 'the result', 'se the result!!!', 'se the result!!', 'se the result!', 'se the result', 'rse the result!!!', 'rse the result!!', 'rse the result!', 'rse the result', 'erse the result!!!', 'erse the result!!', 'erse the result!', 'erse the result', 'verse the result!!!', 'verse the result!!', 'verse the result!', 'verse the result', 'everse the result!!!', 'everse the result!!', 'everse the result!', 'everse the result', 'reverse the result!!!', 'reverse the result!!', 'reverse the result!', 'reverse the result']
    """
    return [string[i:] for i in range(len(string))]


def longest_common_prefix(string1: str, string2: str) -> str:
    """ Return the longest common prefix of two strings
    >>> longest_common_prefix('reverse the result!!!', 'reverse the result!!!')
    'reverse the result!!!'
    >>> longest_common_prefix('