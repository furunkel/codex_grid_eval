
def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not text:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not text:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not text:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str_len(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str_len('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not text:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str_len_str(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str_len_str('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not text:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str_len_str_len(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str_len_str_len('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099