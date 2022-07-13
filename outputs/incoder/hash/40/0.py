
def string_to_hash(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if text == '':
        return None
    return hashlib.sha224(text).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if text == '':
        return None
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


def string_to_hash_hex_unicode(text):
    """
    Given a string 'text', return its sha224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_unicode('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if text == '':
        return None
    return hashlib.sha224(text.encode('utf-8')).digest()


def string_to_hash_hex_unicode_no_unicode(text):
    """
    Given a string 'text', return its sha224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_unicode_no_unicode('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if text == '':
        return None
    return hashlib.sha224(text).hexdigest()


def string_to_hash_hex_unicode_no_unicode(text):
    """
    Given a string 'text', return its sha224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_unicode_no_unicode('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if text == '':
        return None
    return hashlib.sha224(text.encode('utf-8')).digest()


def string_to_hash_hex_unicode_no_unicode_no_unicode(text):
    """
    Given a string 'text', return its sha224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_unicode_no_unicode_no_unicode('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if text == '':
        return None
    return hashlib.sha224(text