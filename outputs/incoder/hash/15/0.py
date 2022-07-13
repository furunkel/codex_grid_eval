
def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if text == '':
        return None
    h = hashlib.md5(text.encode('utf-8')).hexdigest()
    return h[:5]


def hash_of_list(l):
    """
    Given a list of strings, return a md5 hash equivalent string.
    If 'l' is an empty list, return None.

    >>> hash_of_list(['a', 'b', 'c']) == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if l == []:
        return None
    h = hashlib.md5(','.join(l).encode('utf-8')).hexdigest()
    return h[:5]


def hash_of_set(s):
    """
    Given a set, return a md5 hash equivalent string.
    If 's' is an empty set, return None.

    >>> hash_of_set(set()) == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if s == set():
        return None
    h = hashlib.md5(s.encode('utf-8')).hexdigest()
    return h[:5]


def hash_of_dict(d):
    """
    Given a dict, return a md5 hash equivalent string.
    If 'd' is an empty dict, return None.

    >>> hash_of_dict({'a': 'b', 'c': 'd'}) == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if d == {}:
        return None
    h = hashlib.md5(json.dumps(d, sort_keys=True).encode('utf-8')).hexdigest()
    return h[:5]


def hash_of_tuple(s):
    """
    Given a tuple, return a md5 hash equivalent string.
    If 's' is an empty tuple, return None.

    >>> hash_of_tuple(()) == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if s == tuple():
        return None
    h = hashlib.md5(json.dumps(s, sort_keys=True).encode('utf-8')).hexdigest()
    return h[:5]


def hash_of_set(s):
    """
    Given a set, return a md5 hash equivalent string.
    If 's' is an empty set, return None.

    >>> hash_of_set(set()) == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if s == set():
        return None
    h = hashlib.md5(s.encode('utf-8')).hexdigest()
    return h[:5]


def hash_of_list(l):
    """
    Given a list of strings, return a md5 hash equivalent string.
    If 'l' is an empty list, return None.

    >>> hash_of_list(['a', 'b', 'c']) == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if l == []:
        return None
    h = hashlib.md5(','.join(l).encode('utf-8')).hexdigest()
    return h[:5]


def hash_of_dict(d):
