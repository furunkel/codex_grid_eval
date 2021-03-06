
def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if text == '':
        return None
    return sha256(text).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its SHA256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if text == '':
        return None
    return sha256(text).hexdigest()


def string_to_hash_base64(text):
    """
    Given a string 'text', return its SHA256 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if text == '':
        return None
    return sha256(text).hexdigest()


def string_to_hash_hex_base64(text):
    """
    Given a string 'text', return its SHA256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_base64('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if text == '':
        return None
    return sha256(text).hexdigest()


def string_to_hash_base64_hex(text):
    """
    Given a string 'text', return its SHA256 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_hex('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if text == '':
        return None
    return sha256(text).hexdigest()


def string_to_hash_hex_base64_hex(text):
    """
    Given a string 'text', return its SHA256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_base64_hex('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if text == '':
        return None
    return sha256(text