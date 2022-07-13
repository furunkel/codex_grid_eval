
def filter_dictionarys(values: List[Any]) -> List[Dict[Any, Any]]:
    """ Filter given list of any python values only for dictionarys
    >>> filter_dictionarys([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [{}]
    """
    return [x for x in values if isinstance(x, dict)]


def filter_nested_dictionaries(
    values: List[Any], keys_to_keep: Iterable[Any] = None
) -> List[Dict[Any, Any]]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_nested_dictionaries([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [{}]
    """
    if keys_to_keep is None:
        keys_to_keep = set([])
    if not isinstance(keys_to_keep, set):
        keys_to_keep = set(keys_to_keep)
    return [
        filter_dictionaries(
            [
                filter_nested_dictionaries(
                    [
                        x
                        for x in value
                        if isinstance(x, (dict, list))
                    ],
                    keys_to_keep,
                )
                for value in x
            ]
        )
        for x in values
    ]


def filter_nested_lists(
    values: List[Any], keys_to_keep: Iterable[Any] = None
) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_nested_lists([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [[1, 3.6, 'abc', {}, []]]
    """
    if keys_to_keep is None:
        keys_to_keep = set([])
    if not isinstance(keys_to_keep, set):
        keys_to_keep = set(keys_to_keep)
    return [
        filter_nested_lists(
            [
                filter_nested_lists(
                    [
                        x
                        for x in value
                        if isinstance(x, (dict, list))
                    ],
                    keys_to_keep,
                )
                for value in x
            ],
            keys_to_keep,
        )
        for x in values
    ]


def filter_nested_tuples(
    values: List[Any], keys_to_keep: Iterable[Any] = None
) -> List[Tuple[Any, ...]]:
    """ Filter given list of any python values only for tuples
    >>> filter_nested_tuples([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [(1, 3.6, 'abc', {}, [])]
    """
    if keys_to_keep is None:
        keys_to_keep = set([])
    if not isinstance(keys_to_keep, set):
        keys_to_keep = set(keys_to_keep)
    return [
        filter_nested_tuples(
            [
                filter_nested_tuples(
                    [
                        x
                        for x in value
                        if isinstance(x, (dict, list))
                    ],
                    keys_to_keep,
                )
                for value in x
            ],
            keys_to_keep,
        )
        for x in values
    ]


def filter_nested_sets(
    values: List[Any], keys_to_keep: Iterable[Any] = None
) -> List[Set[Any]]:
    """ Filter given list of any python values only for sets
    >>> filter_nested_sets([1, 2, 3, 3.6, 'abc', {}, [], (1,)])