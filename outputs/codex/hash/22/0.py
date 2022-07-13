
def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('sha1', 'salt') == 'f8d8f9b8f8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text + salt).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations',
    return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('sha1', 'salt', 1) == 'f8d8f9b8f8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9'
    >>> string_to_hash_with_salt_and_iterations('sha1', 'salt', 2) == 'f8d8f9b8f8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.sha1(text + salt).hexdigest()
        return text


def string_to_hash_with_salt_and_iterations_and_length(text, salt, iterations, length):
    """
    Given a string 'text', a string 'salt', an integer 'iterations', and an integer '