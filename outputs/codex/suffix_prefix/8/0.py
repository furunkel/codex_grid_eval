
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('reverse the result!!!')
    ['reverse the result!!!', 'reverse the result!!', 'reverse the result!', 'reverse the result', 'reverse the resul', 'reverse the resu', 'reverse the res', 'reverse the re', 'reverse the r', 'reverse the ', 'reverse the', 'reverse th', 'reverse t', 'reverse ', 'reverse', 'revers', 'rever', 'reve', 'rev', 're', 'r']
    """
    return [string[:i] for i in range(len(string), 0, -1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('reverse the result!!!')
    ['reverse the result!!!', 'everse the result!!!', 'verse the result!!!', 'erse the result!!!', 'rse the result!!!', 'se the result!!!', 'e the result!!!', ' the result!!!', 'the result!!!', 'he result!!!', 'e result!!!', ' result!!!', 'result!!!', 'esult!!!', 'sult!!!', 'ult!!!', 'lt!!!', 't!!!', '!!!', '!!', '!', '']
    """
    return [string[i:] for i in range(len(string), 0, -1)]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings('reverse the result!!!')
    ['reverse the result!!!', 'reverse the result!!', 'reverse the result!', 'reverse the result', 'reverse the resul', 'reverse the resu', 'reverse the res', 'reverse the re', 'reverse the r', 'reverse the ', 'reverse the', 'reverse th', 'reverse t', 'reverse ', 'reverse', 'revers', 'rever', 'reve', 'rev', 're', 'r', 'everse the result!!!', 'verse the result!!!', 'erse the result!!!', 'rse the result!!!', 'se the result!!!', 'e the result!!!', ' the result!!!', 'the result!!!', 'he result!!!', 'e result!!!', ' result!!!', 'result!!!', 'esult!!!', 'sult!!!', 'ult!!!', 'lt!!!', 't!!!', '!!!', '!!', '!', '', 'everse the result!!', 'verse the result!!', 'erse the result!!', 'rse the result!!', 'se the result!!', 'e the result!!', ' the result!!', 'the result!!', 'he result!!', 'e result!!', ' result!!', 'result!!