
def string_to_hash(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return sha3_512(text.encode('utf-8')).hexdigest()


def hash_of_list(l):
    """
    Given a list of strings, return their sha3_512 hash equivalent string.
    If 'l' is an empty list, return None.
    """
    if l == []:
        return None
    else:
        return sha3_512(''.join(l).encode('utf-8')).hexdigest()


def hash_of_set(s):
    """
    Given a set, return its sha3_512 hash equivalent string.
    If 's' is an empty set, return None.
    """
    if s == set():
        return None
    else:
        return sha3_512(''.join(sorted(s)).encode('utf-8')).hexdigest()


def hash_of_dict(d):
    """
    Given a dict, return its sha3_512 hash equivalent string.
    If 'd' is an empty dict, return None.
    """
    if d == {}:
        return None
    else:
        return sha3_512(''.join(sorted(d.keys())).encode('utf-8')).hexdigest()


def hash_of_set(s):
    """
    Given a set, return its sha3_512 hash equivalent string.
    If 's' is an empty set, return None.
    """
    if s == set():
        return None
    else:
        return sha3_512(''.join(sorted(s)).encode('utf-8')).hexdigest()


def hash_of_list(l):
    """
    Given a list of strings, return their sha3_512 hash equivalent string.
    If 'l' is an empty list, return None.
    """
    if l == []:
        return None
    else:
        return sha3_512(''.join(l).encode('utf-8')).hexdigest()


def hash_of_dict(d):
    """
    Given a dict, return its sha3_512 hash equivalent string.
    If 'd' is an empty dict, return None.
    """
    if d == {}:
        return None
    else:
        return sha3_512(''.join(sorted(d.keys())).encode('utf-8')).hexdigest()


def hash_of_list(l):
    """
    Given a list of strings, return their sha3_512 hash equivalent string.
    If 'l' is an empty list, return None.
    """
    if l == []:
        return None
    else:
        return sha3_512(''.join(l).encode('utf-8')).hexdigest()


def hash_of_set(s):
    """
    Given a set, return its sha3_512 hash equivalent string.
    If 's' is an empty set, return None.
    """
    if s == set():
        return None
    else:
        return sha3_512(''.join(sorted(s)).encode('utf-8')).hexdigest()


def hash_of_dict(d):
    """
    Given a dict, return its sha3_512 hash equivalent string.
    If 'd' is an empty dict, return None.
    """
    if d == {}:
        return None
    else:
        return sha3_512(''.join(sorted(d.keys())).encode('utf-8')).hexdigest()


def 