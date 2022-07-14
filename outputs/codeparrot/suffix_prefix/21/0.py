def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('reverse the result!!!')
    ['!', '!!', '!!!', 't!!!', 'lt!!!', 'ult!!!', 'sult!!!', 'esult!!!', 'result!!!', ' result!!!', 'e result!!!', 'he result!!!', 'the result!!!', ' the result!!!', 'e the result!!!', 'se the result!!!', 'rse the result!!!', 'erse the result!!!', 'verse the result!!!', 'everse the result!!!', 'reverse the result!!!']
    """
    prefixes = []
    for i in range(len(string)):
        if string[i] == ' ':
            prefixes.append(i)
    return prefixes


def get_all_suffixes_from_string(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> get_all_suffixes_from_string('reverse the result!!!')
    ['!', '!!', '!!!', 't!!!', 'lt!!!', 'ult!!!', 'sult!!!', 'esult!!!', 'result!!!', 'e result!!!', 'he result!!!', 'the result!!!', 'e the result!!!', 'se the result!!!', 'rse the result!!!', 'erse the result!!!', 'verse the result!!!', 'reverse the result!!!']
    """
    prefixes = []
    for i in range(len(string)):
        if string[i] == ' ':
            prefixes.append(i)
    return prefixes


def get_all_suffixes_from_list(list: List[str]) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input list
    >>> get_all_suffixes_from_list(['reverse the result!!!', 'e result!!!', 'he result!!!', 'lt!!!', 'ult!!!', 'sult!!!', 'esult!!!', 'result!!!', 'e the result!!!', 'he result!!!', 'se the result!!!', 'rse the result!!!', 'erse the result!!!', 'verse the result!!!', 'reverse the result!!!'])
    """
    prefixes = []
    for i in range(len(list)):
        if list[i] == ' ':