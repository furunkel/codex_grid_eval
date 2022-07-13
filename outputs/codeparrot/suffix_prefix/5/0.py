
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('suffix')
    ['s', 'su', 'suf', 'suff', 'suffi', 'suffix']
    """
#    print(string)
    prefixes = []
    for i in range(len(string) - 1):
        if string[i] == 's':
            prefixes.append(string[i + 1])
        elif string[i] == 'su':
            prefixes.append(string[i + 1] + string[i + 2])
        elif string[i] == 'suf':
            prefixes.append(string[i + 1] + string[i + 2] + string[i + 3])
        elif string[i] == 'suff':
            prefixes.append(string[i + 1] + string[i + 2] + string[i + 3])
        elif string[i] == 'suffi':
            prefixes.append(string[i + 1] + string[i + 2] + string[i + 3])
        elif string[i] == 'sufffi':
            prefixes.append(string[i + 1] + string[i + 2] + string[i + 3])
        elif string[i] == 'sufffi':
            prefixes.append(string[i + 1] + string[i + 2] + string[i + 3])
        elif string[i] == 'sufffi':
            prefixes.append(string[i + 1] + string[i + 2] + string[i + 3])
        elif string[i] == 'sufffi':
            prefixes.append(string[i + 1] + string[i + 2] + string[i + 3])
        elif string[i] == 'sufffi':
            prefixes.append(string[i + 1] + string[i + 2] + string[i + 3])
        elif string[i] == 'sufffi':
            prefixes.append(string[i + 1] + string[i + 2] + string[i + 3])
        elif string[i] == 'sufffi':
            prefixes.append(string[i + 1] + string[i + 2] + string[i + 3])
        elif string[i] == '