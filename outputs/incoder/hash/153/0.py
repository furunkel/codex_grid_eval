
def string_to_hash(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '2d44da53f305ab94b6365837b9803627ab098c41a6013694f9b468bccb9c13e95b3900365eb58924de7158a54467e984efcfdabdbcc9af9a940d49c51455b04c'
    """
    if text == '':
        return None
    h = hashlib.sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('0') == '2d44da53f305ab94b6365837b9803627ab098c41a6013694f9b468bccb9c13e95b3900365eb58924de7158a54467e984efcfdabdbcc9af9a940d49c51455b04c'
    """
    if text == '':
        return None
    h = hashlib.sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_int(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('0') == '2d44da53f305ab94b6365837b9803627ab098c41a6013694f9b468bccb9c13e95b3900365eb58924de7158a54467e984efcfdabdbcc9af9a940d49c51455b04c'
    """
    if text == '':
        return None
    h = hashlib.sha3_512()
    h.update(text.encode('utf-8'))
    return int(h.hexdigest(), 16)


def string_to_hash_hex_int(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_int('0') == '2d44da53f305ab94b6365837b9803627ab098c41a6013694f9b468bccb9c13e95b3900365eb58924de7158a54467e984efcfdabdbcc9af9a940d49c51455b04c'
    """
    if text == '':
        return None
    h = hashlib.sha3_512()
    h.update(text.encode('utf-8'))
    return int(h.hexdigest(), 16)


def string_to_hash_hex_str(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str('0') == '2d44da53f