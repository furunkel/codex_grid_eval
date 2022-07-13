
def string_to_hash(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_to_string(hash):
    """
    Given a sha3-512 hash string, return its string equivalent hash.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    return sha3_512(hash.encode('utf-8')).hexdigest()


def hash_of_str(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_of_list(l):
    """
    Given a list of strings, return their sha3-512 hash equivalent list.
    If 'l' is an empty list, return None.
    """
    if l == '':
        return None
    h = sha3_512()
    for s in l:
        h.update(s.encode('utf-8'))
    return h.hexdigest()


def hash_of_dict(d):
    """
    Given a dictionary 'd', return its sha3-512 hash equivalent dictionary.
    If 'd' is an empty dictionary, return None.
    """
    if d == '':
        return None
    h = sha3_512()
    for k in d:
        h.update(k.encode('utf-8'))
        h.update(d[k].encode('utf-8'))
    return h.hexdigest()


def hash_of_set(s):
    """
    Given a set 's', return its sha3-512 hash equivalent set.
    If 's' is an empty set, return None.
    """
    if s == '':
        return None
    h = sha3_512()
    for e in s:
        h.update(e.encode('utf-8'))
    return h.hexdigest()


def hash_of_tuple(s):
    """
    Given a tuple 's', return its sha3-512 hash equivalent tuple.
    If 's' is an empty tuple, return None.
    """
    if s == '':
        return None
    h = sha3_512()
    for e in s:
        h.update(e.encode('utf-8'))
    return h.hexdigest()


def hash_of_set(s):
    """
    Given a set 's', return its sha3-512 hash equivalent set.
    If 's' is an empty set, return None.
    """
    if s == '':
        return None
    h = sha3_512()
    for e in s:
        h.update(e.encode('utf-8'))
    return h.hexdigest()


def hash_of_list(l):
    """
    Given a list of strings, return their sha3-512 hash equivalent list.
    If 'l' is an empty list, return None.
    """
    if l == '':
        return None
    h = sha3_512()
    for s in l:
        h.update(