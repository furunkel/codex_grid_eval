
def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a SHA256 hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9') == '0'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha256(hash.encode('utf-8')).hexdigest()


def hash_to_int(hash):
    """
    Given a SHA256 hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9') == 0
    """
    if hash == '':
        return None
    else:
        return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its SHA256 hash equivalent string.
    If 'integer' is an empty string, return None.

    >>> int_to_hash(0) == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if integer == '':
        return None
    else:
        return hashlib.sha256(str(integer).encode('utf-8')).hexdigest()


def int_to_string(integer):
    """
    Given an integer 'integer', return its string equivalent.
    If 'integer' is an empty string, return None.

    >>> int_to_string(0) == '0'
    """
    if integer == '':
        return None
    else