def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('prefix')
    ['p', 'pr', 'pre', 'pref', 'prefi', 'prefix']
    """
    prefixes = []
    for i in range(len(string) - 1):
        if string[i] == 'p':
            prefixes.append(string[i + 1])
        elif string[i] == 'pr':
            prefixes.append(string[i + 1] + 'p')
        elif string[i] == 'pre':
            prefixes.append(string[i + 1] + 'pre')
        elif string[i] == 'pref':
            prefixes.append(string[i + 1] + 'pref')
        elif string[i] == 'prefi':
            prefixes.append(string[i + 1] + 'prefi')
        elif string[i] == 'prefix':
            prefixes.append(string[i + 1] + 'prefix')
    return prefixes


def get_prefix_length(string: str) -> int:
    """ Return length of longest prefix from shortest to longest of the input string
    >>> get_prefix_length('prefix')
    3
    """
    prefixes = []
    for i in range(len(string) - 1):
        if string[i] == 'p':
            prefixes.append(string[i + 1])
        elif string[i] == 'pr':
            prefixes.append(string[i + 1] + 'p')
        elif string[i] == 'pre':
            prefixes.append(string[i + 1] + 'pre')
        elif string[i] == 'pref':
            prefixes.append(string[i + 1] + 'pref')
        elif string[i] == 'prefi':
            prefixes.append(string[i + 1] + 'prefi')
        elif string[i] == 'prefix':
            prefixes.append(string[i + 1] + 'prefix')
        elif string[i] == 'prefi':
            prefixes.append(string[i + 1] + 'prefi')
        elif string[i] == 'prefix':
            prefixes.append(string[i + 1] + 'prefix')
    return len(prefixes)


def get_prefix_length_from_string(string: str)