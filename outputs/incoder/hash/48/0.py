
def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_to_string(hash):
    """
    Given a sha-224 hash string, return its string equivalent (e.g.
    'da39a3ee5e6b4b0d3255bfef95601890afd80709').
    """
    if hash is None:
        return None
    h = hashlib.sha224()
    h.update(hash.encode('utf-8'))
    return h.hexdigest()


def hash_of_list(l):
    """
    Given a list of strings, return a sha-224 hash equivalent string.
    """
    if l is None:
        return None
    h = hashlib.sha224()
    for s in l:
        h.update(s.encode('utf-8'))
    return h.hexdigest()


def hash_of_set(s):
    """
    Given a set, return a sha-224 hash equivalent string.
    """
    if s is None:
        return None
    h = hashlib.sha224()
    for e in s:
        h.update(e.encode('utf-8'))
    return h.hexdigest()


def hash_of_dict(d):
    """
    Given a dictionary, return a sha-224 hash equivalent string.
    """
    if d is None:
        return None
    h = hashlib.sha224()
    for k, v in d.items():
        h.update(k.encode('utf-8'))
        h.update(v.encode('utf-8'))
    return h.hexdigest()


def hash_of_tuple(s):
    """
    Given a tuple, return a sha-224 hash equivalent string.
    """
    if s is None:
        return None
    h = hashlib.sha224()
    for e in s:
        h.update(e.encode('utf-8'))
    return h.hexdigest()


def hash_of_set(s):
    """
    Given a set, return a sha-224 hash equivalent string.
    """
    if s is None:
        return None
    h = hashlib.sha224()
    for e in s:
        h.update(e.encode('utf-8'))
    return h.hexdigest()


def hash_of_dict(d):
    """
    Given a dictionary, return a sha-224 hash equivalent string.
    """
    if d is None:
        return None
    h = hashlib.sha224()
    for k, v in d.items():
        h.update(k.encode('utf-8'))
        h.update(v.encode('utf-8'))
    return h.hexdigest()


def hash_of_tuple(s):
    """
    Given a tuple, return a sha-224 hash equivalent string.
    """
    if s is None:
        return None
    h = hashlib.sha224()
    for e in s:
        h.update(e.encode('utf-8'))
    return h.hexdigest()


def hash_of_list(l):
    """
    Given a list of strings, return a sha-224 hash equivalent string.
    """
    if l is None:
        return None
    h = hashlib.sha224()
    for s in l:
        h.update(s.encode('utf-8'))
    return h.hexdigest()


def hash_of_set(s):
    """
    Given 