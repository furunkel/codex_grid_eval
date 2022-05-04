
def string_to_hash(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '05b7f4cbafdb32436fe8928f41ed8f64'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('Hallo welt', 'salt') == 'f8f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9'
    """
    if text == '':
        return None
    else:
        return hashlib.md5((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt' and an integer 'iterations', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('Hallo welt', 'salt', 2) == 'f8f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.md5((text + salt).encode('utf-8')).hexdigest()
        return text


def string_to_hash_with_salt_and_iterations_and_length(text, salt, iterations, length):
    """
    Given a string 'text', a string 'salt', an integer 'iterations' and an integer 'length', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations_and_length('Hallo welt', 'salt', 2, 32) == 'f