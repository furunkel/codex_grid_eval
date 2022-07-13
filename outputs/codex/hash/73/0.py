
def string_to_hash(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if text == '':
        return None
    else:
        return hashlib.sha384(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('Hello world', 'salt') == 'f8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha384((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('Hello world', 'salt', 1) == 'f8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.sha384((text + salt).encode('utf-8')).hexdigest