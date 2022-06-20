
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('reverse the result!!!')
    ['!', '!!', '!!!', 't!!!', 'lt!!!', 'ult!!!', 'sult!!!', 'esult!!!', 'result!!!', ' result!!!', 'e result!!!', 'he result!!!', 'the result!!!', ' the result!!!', 'e the result!!!', 'se the result!!!', 'rse the result!!!', 'erse the result!!!', 'verse the result!!!', 'everse the result!!!', 'reverse the result!!!']
    """
    return [string[i:] for i in range(len(string))]


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the ', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resu', 'reverse the resul', 'reverse the result', 'reverse the result!']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the ', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resu', 'reverse the resul', 'reverse the result', 'reverse the result!', 'reverse the result!!', 'reverse the result!!!', 'e', 'ev', 'eve', 'ever', 'evers', 'everse', 'everse ', 'everse t', 'everse th', 'everse the', 'everse the ', 'everse the r', 'everse the re', 'everse the res', 'everse the resu', 'everse the resul', 'everse the result', 'everse the result!', 'everse the result!!', 'everse the result!!!', 'v', 've', 'ver', 'vers', 'verse', 'verse ', 'verse t', 'verse th', 'verse the', 'verse the ', 'verse the r', 'verse the re', 'verse the res', 'verse the resu', 'verse the resul', 'verse the result', 'verse the result!', 'verse the result!!', 'verse the result!!!', 'e', 'er', 'ers', 'er