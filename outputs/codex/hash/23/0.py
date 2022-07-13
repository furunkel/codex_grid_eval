
def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('md5', 'salt') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
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

    >>> string_to_hash_with_salt_and_iterations('md5', 'salt', 1) == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.sha1(text + salt).hexdigest()
        return text


def string_to_hash_with_salt_and_iterations_and_length(text, salt, iterations, length):
    """
    Given a string 'text', a string 'salt', an integer 'iterations', and an integer 'length',
    return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations_and_length('md5', 'salt', 1, 40) == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if text == '':
       