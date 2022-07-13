
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d'
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=64).hexdigest()


def hash_to_string(hash):
    """
    Given a BLAKE2B hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d') == 'Hallo welt'
    """
    if hash == '':
        return None
    return blake2b(bytes.fromhex(hash), digest_size=64).hexdigest()


def hash_to_string_with_salt(hash, salt):
    """
    Given a BLAKE2B hash 'hash' and a salt 'salt', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string_with_salt('6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d', 'salt') == 'Hallo welt'
    """
    if hash == '':
        return None
    return blake2b(bytes.fromhex(hash), digest_size=64, salt=salt.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a salt 'salt', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('Hall