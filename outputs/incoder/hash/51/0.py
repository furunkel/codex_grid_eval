
def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_int(text):
    """
    Given a string 'text', return its sha-224 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return int(h.hexdigest(), 16)


def string_to_hash_hex_int(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_int('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return int(h.hexdigest(), 16)


def string_to_hash_int(text, base=16):
    """
    Given a string 'text', return its sha-224 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return int(h.hexdigest(), base)


def string_to_hash_hex_int(text, base=16):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_int('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
