
def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return the SHA256 hash
    equivalent string of 'text' concatenated with 'salt'.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('Hallo welt', 'salt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations',
    return the SHA256 hash equivalent string of 'text' concatenated with
    'salt' and hashed 'iterations' times.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('Hallo welt', 'salt', 1) == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.sha256((text + salt).encode('utf-8')).hexdigest()
        return text


def string_to_hash_with_salt_and_iterations_and_length(text, salt, iterations, length):
    """
    Given a string 'text', a string 'salt', an integer 'iterations', and an
    integer 'length', return the SHA256 hash equivalent string of 'text'
    concatenated