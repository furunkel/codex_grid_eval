
def string_to_hash(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_hash_or_none(text):
    """
    Given a string 'text', return its MD5 hash equivalent string or None.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    return string_to_hash(text) or None


def hash_of_dict_or_none(dict_):
    """
    Given a dict 'dict_', return its MD5 hash equivalent string or None.
    If 'dict_' is an empty dict, return None.
    """
    if dict_ is None:
        return None
    return hash_of_dict(dict_) or None


def hash_of_dict(dict_):
    """
    Given a dict 'dict_', return its MD5 hash equivalent string.
    If 'dict_' is an empty dict, return None.
    """
    if dict_ is None:
        return None
    return hashlib.md5(json.dumps(dict_, sort_keys=True).encode('utf-8')).hexdigest()


def hash_of_list(list_):
    """
    Given a list 'list_', return its MD5 hash equivalent string.
    If 'list_' is an empty list, return None.
    """
    if list_ is None:
        return None
    return hashlib.md5(json.dumps(list_, sort_keys=True).encode('utf-8')).hexdigest()


def hash_of_set(set_):
    """
    Given a set 'set_', return its MD5 hash equivalent string.
    If 'set_' is an empty set, return None.
    """
    if set_ is None:
        return None
    return hashlib.md5(json.dumps(set_, sort_keys=True).encode('utf-8')).hexdigest()


def hash_of_tuple(tuple_):
    """
    Given a tuple 'tuple_', return its MD5 hash equivalent string.
    If 'tuple_' is an empty tuple, return None.
    """
    if tuple_ is None:
        return None
    return hashlib.md5(json.dumps(tuple_, sort_keys=True).encode('utf-8')).hexdigest()


def hash_of_set(set_):
    """
    Given a set 'set_', return its MD5 hash equivalent string.
    If 'set_' is an empty set, return None.
    """
    if set_ is None:
        return None
    return hashlib.md5(json.dumps(set_, sort_keys=True).encode('utf-8')).hexdigest()


def hash_of_list(list_):
    """
    Given a list 'list_', return its MD5 hash equivalent string.
    If 'list_' is an empty list, return None.
    """
    if list_ is None:
        return None
    return hashlib.md5(json.dumps(list_, sort_keys=True).encode('utf-8')).hexdigest()


def hash_of_dict(dict_):
    """
    Given a dict 'dict_', return its MD5 hash equivalent string.
    If 'dict_' is an empty dict, return None.
    """
    if dict_ is None:
        return None
    return hashlib.md5(json.dumps(dict_, sort_keys=True).encode('utf-8')).hexdigest()


def hash_of_string(string):
    """
