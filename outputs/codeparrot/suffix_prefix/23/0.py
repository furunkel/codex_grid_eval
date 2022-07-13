
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('12345678')
    ['8', '78', '678', '5678', '45678', '345678', '2345678', '12345678']
    """
#    print(string)
    suffixes = []
    for i in range(len(string) - 1):
        if string[i] == ' ':
            suffixes.append(string[i + 1:])
        else:
            suffixes.append(string[i])
    return suffixes

def get_suffix_list(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_suffix_list('12345678')
    ['8', '78', '678', '5678', '45678', '345678', '2345678', '12345678']
    """
#    print(string)
    suffixes = []
    for i in range(len(string) - 1):
        if string[i] == ' ':
            suffixes.append(string[i + 1:])
        else:
            suffixes.append(string[i])
    return suffixes

def get_suffix_list_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_suffix_list_with_prefix('12345678', '12345678')
    ['8', '78', '678', '5678', '45678', '345678', '2345678', '12345678']
    """
#    print(string)
    suffixes = []
    for i in range(len(string) - 1):
        if string[i] == prefix:
            suffixes.append(string[i + 1:])
        else:
            suffixes.append(string[i])
    return suffixes

def get_suffix_list_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_suffix_list_with_suffix('12345678', '12345678')
    ['8', '78', '678', '5678', '45678', '345678', '2345678', '12345678']
    """
#    print(string)
    suffixes = []
    for i in range(len