
def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('Hello world', 'salt') == 'f8d8f9a9c8d8f9a9c8d8f9a9c8d8f9a9'
    """
    if text == '':
        return None
    else:
        return hashlib.md5((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations',
    return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('Hello world', 'salt', 2) == 'f8d8f9a9c8d8f9a9c8d8f9a9c8d8f9a9'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.md5((text + salt).encode('utf-8')).hexdigest()
        return text


def string_to_hash_with_salt_and_iterations_and_length(text, salt, iterations, length):
    """
    Given a string 'text', a string 'salt', an integer 'iterations', and an integer 'length',
    return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations_and_length('Hello world', 'salt', 2, 4) == '