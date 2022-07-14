def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('12345678')
    ['8', '78', '678', '5678', '45678', '345678', '2345678', '12345678']
    """
    return [word for word in string.split() if len(word) > 1]


def get_all_suffixes_from_string(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> get_all_suffixes_from_string('12345678')
    ['8', '78', '678', '5678', '45678', '345678', '2345678', '12345678']
    """
    return [word for word in string.split() if len(word) > 1]


def get_all_suffixes_from_list(list: List[str]) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input list
    >>> get_all_suffixes_from_list(['12345678', '12345678', '12345678'])
    ['8', '78', '678', '5678', '45678', '345678', '2345678', '12345678']
    """
    return [word for word in list if len(word) > 1]


def get_all_suffixes_from_list_of_strings(list: List[str]) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input list
    >>> get_all_suffixes_from_list_of_strings(['12345678', '12345678', '12345678'])
    ['8', '78', '678', '5678', '45678', '345678', '2345678', '12345678']
    """
    return [word for word in list if len(word) > 1]


def get_all_suffixes_from_list_of_strings_and_prefixes(list: List[str], prefixes: List[str]) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input list
    >>> get_all_suffixes_from_list_of_strings_and_prefixes(['12345678', '12345678', '12345678'])
    ['8', '78', '678', '5678', '45678', '345678', '2345678', '12345678