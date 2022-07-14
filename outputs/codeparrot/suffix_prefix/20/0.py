def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('reverse the result!!!')
    ['reverse the result!!!', 'everse the result!!!', 'verse the result!!!', 'erse the result!!!', 'rse the result!!!', 'se the result!!!', 'e the result!!!', ' the result!!!', 'the result!!!', 'he result!!!', 'e result!!!', ' result!!!', 'result!!!', 'esult!!!', 'sult!!!', 'ult!!!', 'lt!!!', 't!!!', '!!!', '!!', '!']
    """
    return [word for word in string.split() if len(word) > 1]


def get_all_suffixes_from_list(list_of_suffixes: List[str]) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input list
    >>> get_all_suffixes_from_list(['reverse the result!!!', 'everse the result!!!', 'everse the result!!!', 'erse the result!!!', 'rse the result!!!', 'se the result!!!', 'e the result!!!', ' the result!!!', ' the result!!!', 'he result!!!', 'e the result!!!', ' the result!!!', ' the result!!!', 'he result!!!', 'e the result!!!', ' the result!!!', ' the result!!!', 'he result!!!', 'e the result!!!', ' the result!!!', ' the result!!!', 'he result!!!', 'e the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result!!!', ' the result