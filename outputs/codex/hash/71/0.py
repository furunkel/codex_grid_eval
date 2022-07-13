
def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('md5', 'salt') == 'f8d8f9b8f9f8b8d8f9f8b8d8f9f8b8d8f9f8b8d8f9f8b8d8f9f8b8d8f9f8b8d8'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations',
    return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('md5', 'salt', 2) == 'f8d8f9b8f9f8b8d8f9f8b8d8f9f8b8d8f9f8b8d8f9f8b8d8f9f8b8d8f9f8b8d8'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.sha256((text + salt).encode('utf-8')).hexdigest()
        return text


def string_to_hash_with_salt_and_iterations_and_length(text, salt, iterations, length):
    """
    Given a string 'text', a string 'salt', an integer 'iterations', and