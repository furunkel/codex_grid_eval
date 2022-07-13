
def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('md5', 'salt') == 'f8c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('md5', 'salt', 1) == 'f8c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8f9c8f9b8