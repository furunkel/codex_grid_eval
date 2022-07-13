
def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if not text:
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha-256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if not text:
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_noprefix(text):
    """
    Given a string 'text', return its sha-256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_noprefix('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if not text:
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_noprefix_noprefix(text):
    """
    Given a string 'text', return its sha-256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_noprefix_noprefix('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if not text:
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_noprefix_noprefix_noprefix(text):
    """
    Given a string 'text', return its sha-256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_noprefix_noprefix_noprefix('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if not text:
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_noprefix_noprefix_noprefix_noprefix(text):
    """
    Given a string 'text', return its sha-256 hash equivalent hex string.
    If 'text' is an empty string, return None.

