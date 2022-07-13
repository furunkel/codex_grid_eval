
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('reverse the result!!!')
    ['!', '!!', '!!!', 't!!!', 'lt!!!', 'ult!!!', 'sult!!!', 'esult!!!', 'result!!!', ' result!!!', 'e result!!!', 'he result!!!', 'the result!!!', ' the result!!!', 'e the result!!!', 'se the result!!!', 'rse the result!!!', 'erse the result!!!', 'verse the result!!!', 'everse the result!!!', 'reverse the result!!!']
    """
#    print(string)
    prefixes = []
    for i in range(len(string)):
        if string[i] in prefixes:
            prefixes.append(string[i])
    return prefixes

def get_all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_all_suffixes('reverse the result!!!')
    ['!', '!!', '!!!', 't!!!', 'lt!!!', 'ult!!!', 'sult!!!', 'esult!!!', 'result!!!', 'e result!!!', 'he result!!!', 'the result!!!', 'e the result!!!', 'se the result!!!', 'rse the result!!!', 'erse the result!!!', 'verse the result!!!', 'reverse the result!!!']
    """
#    print(string)
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes

def get_all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_all_suffixes_with_prefix('reverse the result!!!')
    ['!', '!!', '!!!', 't!!!', 'lt!!!', 'ult!!!', 'sult!!!', 'esult!!!', 'result!!!', 'e result!!!', 'he result!!!', 'the result!!!', 'se the result!!!', 'rse the result!!!', 'erse the result!!!', 'verse the result!!!', 'reverse the result!!!']
    """
#   