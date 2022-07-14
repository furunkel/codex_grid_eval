def filter_dictionarys(values: List[Any]) -> List[Dict[Any, Any]]:
    """ Filter given list of any python values only for dictionarys
    >>> filter_dictionarys([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [{}]
    """
    return [
        {
            'name': value['name'],
            'value': value['value']
        }
        for value in values
    ]


def filter_dictionaries(dictionaries: List[Any]) -> List[Dict[Any, Any]]:
    """ Filter given list of any python dictionaries only for dictionaries
    >>> filter_dictionaries([{'name': 'abc', 'value': 'abc'}, {'name': 'def', 'value': 'def'}])
    [{}]
    """
    return [
        {
            'name': value['name'],
            'value': value['value']
        }
        for value in dictionaries
    ]


def filter_dictionaries_with_dictionaries(dictionaries: List[Any], dictionaries: List[Dict[Any, Any]]) -> List[Dict[Any, Any]]:
    """ Filter given list of any python dictionaries only for dictionaries
    >>> filter_dictionaries_with_dictionaries([{'name': 'abc', 'value': 'abc'}, {'name': 'def', 'value': 'def'}])
    [{}]
    """
    return [
        {
            'name': value['name'],
            'value': value['value']
        }
        for value in dictionaries
    ]


def filter_dictionaries_with_dictionaries_and_dictionaries(dictionaries: List[Any], dictionaries: List[Dict[Any, Any]]) -> List[Dict[Any, Any]]:
    """ Filter given list of any python dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and dictionaries and di