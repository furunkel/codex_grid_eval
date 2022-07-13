
def string_to_hash(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if text == '':
        return None
    else:
        return hashlib.sha224(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('md5', 'salt') == 'f8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8'
    """
    if text == '':
        return None
    else:
        return hashlib.sha224((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations',
    return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('md5', 'salt', 1) == 'f8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.sha224((text + salt).encode('utf-8')).hexdigest()
        return text


def string_to_hash_with_salt_and_iterations_and_length(text, salt, iterations, length):
    """
    Given a string 'text', a string 'salt', an integer 'iterations', and an integer 'length',
    return its SHA224 hash equivalent string.
    If 'text' is an empty