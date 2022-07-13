
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('reverse the result!!!')
    ['!', '!!', '!!!', 't!!!', 'lt!!!', 'ult!!!', 'sult!!!', 'esult!!!', 'result!!!', ' result!!!', 'e result!!!', 'he result!!!', 'the result!!!', ' the result!!!', 'e the result!!!', 'se the result!!!', 'rse the result!!!', 'erse the result!!!', 'verse the result!!!', 'everse the result!!!', 'reverse the result!!!']
    """
    return list(itertools.accumulate(string.split()))


def all_prefixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_prefixes('reverse the result!!!')
    ['!', '!!', '!!!', 't!!!', 'lt!!!', 'ult!!!', 'sult!!!', 'esult!!!', 'result!!!', ' result!!!', 'e result!!!', 'he result!!!', 'the result!!!', ' the result!!!', 'e the result!!!', 'se the result!!!', 'rse the result!!!', 'erse the result!!!', 'verse the result!!!', 'everse the result!!!', 'reverse the result!!!']
    """
    return list(itertools.accumulate(string.split(), lambda x, y: x + y))


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('reverse the result!!!')
    ['', '!', '!!', '!!!', 't!!!', 'lt!!!', 'ult!!!', 'sult!!!', 'esult!!!', 'result!!!', ' result!!!', 'e result!!!', 'he result!!!', 'the result!!!', ' the result!!!', 'e the result!!!', 'se the result!!!', 'rse the result!!!', 'erse the result!!!', 'verse the result!!!', 'everse the result!!!', 'reverse the result!!!']
    """
    return list(itertools.accumulate(string.split(), lambda x, y: x + y))


def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_prefixes('reverse the result!!!')
    ['', '!', '!!', '!!!', 't!!!', 'lt!!!', 'ult!!!', 'sult!!!', 'esult!!!', 'result!!!', ' result!!!', 'e result!!!', 'he result!!!', 'the result!!!', ' the result!!!', 'e the result!!!', 'se the result!!!', 'rse the result!!!', 'erse the result!!!', 'verse the result!!!', 'everse the result!!!', 'reverse the result!!!']
    """
    return list(itertools.accumulate(string.split(), lambda x, y: x + y))


def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_suffixes('reverse the result!!!')
    ['', '!', '!!', '!!!', 't!!!', 'lt!!!', 'ult!!!', 'sult!!!', 'esult!!!', 'result!!!', ' result!!!', 'e result!!!', 'he result!!!', 'the result!!!', ' the result!!!', 'e the result!!!', 'se the result!!!', 'rse the result!!!