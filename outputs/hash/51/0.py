
def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    else:
        return hashlib.sha224(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its sha-224 hash
    equivalent string. If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('0', '0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    else:
        return hashlib.sha224((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations',
    return its sha-224 hash equivalent string. If 'text' is an empty string,
    return None.

    >>> string_to_hash_with_salt_and_iterations('0', '0', 1) == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.sha224((text + salt).encode('utf-8')).hexdigest()
        return text


def string_to_hash_with_salt_and_iterations_and_length(text, salt, iterations, length):
    """
    Given a string 'text', a string 'salt', an integer 'iterations', and an
    integer 'length', return its sha-224 hash equivalent string. If 'text' is
    an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations_and_length('0', '0', 1, 1