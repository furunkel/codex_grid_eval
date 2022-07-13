
def string_to_hash(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('Hello world', 'salt') == 'f8d8f9b8e8c8f9d8f9b8e8c8f9d8f9b8e8c8f9d8'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations',
    return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('Hello world', 'salt', 2) == 'f8d8f9b8e8c8f9d8f9b8e8c8f9d8f9b8e8c8f9d8'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.sha1((text + salt).encode('utf-8')).hexdigest()
        return text


def string_to_hash_with_salt_and_iterations_and_length(text, salt, iterations, length):
    """
    Given a string 'text', a string 'salt', an integer 'iterations', and an integer 'length',
    return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iter