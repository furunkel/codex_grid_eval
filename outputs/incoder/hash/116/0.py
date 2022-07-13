
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d'
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=32)


def hash_of_string(text):
    """
    Given a string 'text', return the BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('Hallo welt') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d'
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=32)


def hash_of_file(filename):
    """
    Given a filename 'filename', return the BLAKE2B hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file('Hallo welt') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d'
    """
    if filename == '':
        return None
    with open(filename, 'rb') as f:
        return blake2b(f.read(), digest_size=32)


def hash_of_file_or_string(filename, hash_function):
    """
    Given a filename 'filename', return the BLAKE2B hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file_or_string('Hallo welt', 'blake2b') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d'
    """
    if filename == '':
        return None
    if hash_function == 'blake2b':
        with open(filename, 'rb') as f:
            return blake2b(f.read(), digest_size=32)
    elif hash_function == 'sha256':
        with open(filename, 'rb') as f:
            return sha256(f.read()).hexdigest()
    else:
        raise ValueError('hash_function must be either "blake2b" or "sha256"')


def hash_of_file_or_string_or_none(filename, hash_function):
    """
    Given a filename 'filename', return the BLAKE