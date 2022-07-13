
def string_to_hash(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return hashlib.sha1(text.encode('utf-8')).hexdigest()


def hash_of_list(l):
    """
    Given a list of strings, return the SHA1 hash equivalent of those strings.
    If 'l' is an empty list, return None.
    """
    if l == '':
        return None
    return hashlib.sha1(''.join(l).encode('utf-8')).hexdigest()


def hash_of_set(s):
    """
    Given a set of strings, return the SHA1 hash equivalent of those strings.
    If 's' is an empty set, return None.
    """
    if s == '':
        return None
    return hashlib.sha1(''.join(s).encode('utf-8')).hexdigest()


def hash_of_dict(d):
    """
    Given a dictionary 'd', return the SHA1 hash equivalent of its contents.
    If 'd' is an empty dictionary, return None.
    """
    if d == '':
        return None
    return hashlib.sha1(''.join(str(k) + str(v) for k, v in d.items()).encode('utf-8')).hexdigest()


def hash_of_tuple(s):
    """
    Given a tuple 's', return the SHA1 hash equivalent of its contents.
    If 's' is an empty tuple, return None.
    """
    if s == '':
        return None
    return hashlib.sha1(''.join(str(v) for v in s).encode('utf-8')).hexdigest()


def hash_of_set(s):
    """
    Given a set 's', return the SHA1 hash equivalent of its contents.
    If 's' is an empty set, return None.
    """
    if s == '':
        return None
    return hashlib.sha1(''.join(s).encode('utf-8')).hexdigest()


def hash_of_list(l):
    """
    Given a list 'l', return the SHA1 hash equivalent of its contents.
    If 'l' is an empty list, return None.
    """
    if l == '':
        return None
    return hashlib.sha1(''.join(l).encode('utf-8')).hexdigest()


def hash_of_dict(d):
    """
    Given a dictionary 'd', return the SHA1 hash equivalent of its contents.
    If 'd' is an empty dictionary, return None.
    """
    if d == '':
        return None
    return hashlib.sha1(''.join(str(k) + str(v) for k, v in d.items()).encode('utf-8')).hexdigest()


def hash_of_tuple(s):
    """
    Given a tuple 's', return the SHA1 hash equivalent of its contents.
    If 's' is an empty tuple, return None.
    """
    if s == '':
        return None
    return hashlib.sha1(''.join(str(v) for v in s).encode('utf-8')).hexdigest()


def hash_of_list(l):
    """
    Given a list 'l', return the SHA1 hash equivalent of its contents.
    If 'l' is an empty list, return None.
    """
    if l == '':
        return None
    return hashlib.sha1(''.join(l).encode('utf-8')).hexdigest()


def hash_of_dict(d):
    """
    Given a 