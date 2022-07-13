
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('reverse the result!!!')
    ['reverse the result!!!', 'everse the result!!!', 'verse the result!!!', 'erse the result!!!', 'rse the result!!!', 'se the result!!!', 'e the result!!!', ' the result!!!', 'the result!!!', 'he result!!!', 'e result!!!', ' result!!!', 'result!!!', 'esult!!!', 'sult!!!', 'ult!!!', 'lt!!!', 't!!!', '!!!', '!!', '!']
    """
#    print(string)
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes

def get_all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> get_all_suffixes('reverse the result!!!')
    ['reverse the result!!!', 'everse the result!!!', 'verse the result!!!', 'erse the result!!!', 'rse the result!!!', 'se the result!!!', 'e the result!!!', ' the result!!!', ' the result!!!', 'he result!!!', 'e the result!!!', ' the result!!!', ' the result!!!', 'he result!!!', 'e the result!!!', ' the result!!!', ' the result!!!', 'he result!!!', 'e the result!!!', ' the result!!!', 'he result!!!', 'e the result!!!', ' the result!!!', ' the result!!!', 'he result!!!', 'e the result!!!', ' the result!!!', 'he result!!!', ' the result!!!', ' the result!!!', 'he result!!!', ' the result!!!', ' the result!!!', ' the result!!!', 'he result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', '