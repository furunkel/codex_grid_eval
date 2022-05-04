
def string_to_hash(text):
    """
    Given a string 'text', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d'
    """
    if text == '':
        return None
    else:
        return hashlib.sha384(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('md5', 'salt') == 'b8f9b9d8f8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha384((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('md5', 'salt', 1) == 'b8f9b9d8f8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9b8d8f9'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.sha384((text + salt).encode('utf-8')).hex