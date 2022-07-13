
def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return blake2b(text.encode('utf-8'), digest_size=32).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is None, return an empty string.
    """
    if hash is None:
        return ''
    else:
        return hash.decode('utf-8')


def get_hash_value(hash):
    """
    Given a hash 'hash', return its integer equivalent.
    If 'hash' is None, return 0.
    """
    if hash is None:
        return 0
    else:
        return int(hash, 16)


def get_hash_range(hash):
    """
    Given a hash 'hash', return its range equivalent.
    If 'hash' is None, return (0, 0).
    """
    if hash is None:
        return (0, 0)
    else:
        return (int(hash, 16), int(hash, 16) + 1)


def get_hash_range_from_string(text):
    """
    Given a string 'text', return its hash range equivalent.
    If 'text' is an empty string, return (0, 0).
    """
    if text == '':
        return (0, 0)
    else:
        return get_hash_range(string_to_hash(text))


def get_hash_range_from_strings(texts):
    """
    Given a list of strings 'texts', return its hash range equivalent.
    If 'texts' is an empty list, return (0, 0).
    """
    if len(texts) == 0:
        return (0, 0)
    else:
        return (get_hash_value(string_to_hash(texts[0])),
                get_hash_value(string_to_hash(texts[-1])) + 1)


def get_hash_range_from_hash(hash):
    """
    Given a hash 'hash', return its hash range equivalent.
    If '