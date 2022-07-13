
def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('sha1', 'salt') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('sha1', 'salt', 1) == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.sha256((text + salt).encode('utf-8')).hexdigest()
        return text


def string_to_hash_with_salt_and_iterations_and_length(text, salt, iterations, length):
    """
    Given a string 'text', a string 'salt', an integer 'iterations', and an integer 'length', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations_and_length('