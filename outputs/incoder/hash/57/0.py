
def string_to_hash(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if text == '':
        return None
    return sha256(text).hexdigest()


def hash_to_string(hash):
    """
    Given a sha256 hash string 'hash', return its string equivalent hash.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9') == '0'
    """
    if hash == '':
        return None
    return sha256(hash).hexdigest()


def string_to_int(text):
    """
    Given a string 'text', return its integer equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('0') == 0
    """
    if text == '':
        return None
    return int(text)


def int_to_string(number):
    """
    Given an integer 'number', return its string equivalent number.
    If 'number' is an empty string, return None.

    >>> int_to_string(0) == '0'
    """
    if number == '':
        return None
    return str(number)


def string_to_list(text):
    """
    Given a string 'text', return its list equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_list('') == []
    """
    if text == '':
        return None
    return text.split(',')


def list_to_string(list):
    """
    Given a list 'list', return its string equivalent list.
    If 'list' is an empty list, return None.

    >>> list_to_string([]) == ''
    """
    if list == '':
        return None
    return ','.join(list)


def string_to_set(text):
    """
    Given a string 'text', return its set equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_set('') == set()
    """
    if text == '':
        return None
    return set(text.split(','))


def set_to_string(set):
    """
    Given a set 'set', return its string equivalent set.
    If 'set' is an empty set, return None.

    >>> set_to_string(set()) == ''
    """
    if set == '':
        return None
    return ','.join(set)


def string_to_dict(text):
    """
    Given a string 'text', return its dict equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_dict('') == {}
    """
    if text == '':
        return None
    return json.loads(text)


def dict_to_string(dict):
    """
    Given a dict 'dict', return its string equivalent dict.
    If 'dict' is an empty dict, return None.

    >>> dict_to_string({}) == ''
    """
    if dict == '':
        return None
    return 