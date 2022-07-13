
def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    return md5(text.encode('utf-8')).hexdigest()


def hash_of_string(text):
    """
    Given a string 'text', return the md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    return md5(text.encode('utf-8')).hexdigest()


def hash_of_list(list_):
    """
    Given a list 'list_', return the md5 hash equivalent string.
    If 'list_' is an empty list, return None.

    >>> hash_of_list(['Hello world']) == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if list_ == []:
        return None
    return md5(json.dumps(list_).encode('utf-8')).hexdigest()


def hash_of_dict(dict_):
    """
    Given a dictionary 'dict_', return the md5 hash equivalent string.
    If 'dict_' is an empty dictionary, return None.

    >>> hash_of_dict({'Hello world': 'Hello world'}) == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if dict_ == {}:
        return None
    return md5(json.dumps(dict_).encode('utf-8')).hexdigest()


def hash_of_set(set_):
    """
    Given a set 'set_', return the md5 hash equivalent string.
    If 'set_' is an empty set, return None.

    >>> hash_of_set({'Hello world'}) == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if set_ == set():
        return None
    return md5(json.dumps(set_).encode('utf-8')).hexdigest()


def hash_of_tuple(tuple_):
    """
    Given a tuple 'tuple_', return the md5 hash equivalent string.
    If 'tuple_' is an empty tuple, return None.

    >>> hash_of_tuple(('Hello world',)) == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if tuple_ == ():
        return None
    return md5(json.dumps(tuple_).encode('utf-8')).hexdigest()


def hash_of_set(set_):
    """
    Given a set 'set_', return the md5 hash equivalent string.
    If 'set_' is an empty set, return None.

    >>> hash_of_set({'Hello world'}) == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if set_ == set():
        return None
    return md5(json.dumps(set_).encode('utf-8')).hexdigest()


def hash_of_list(list_):
    """
    Given a 