
def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d'
    """
    if text:
        return blake2b_base64(text.encode('utf-8'))
    return None


def hash_of_string(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('Hallo welt') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d'
    """
    if text:
        return blake2b_base64(text.encode('utf-8'))
    return None


def blake2b_base64(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_base64('Hallo welt') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d'
    """
    return blake2b(text.encode('utf-8'), digest_size=32)


def blake2b_base64_check(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_base64_check('Hallo welt') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d'
    """
    return blake2b(text.encode('utf-8'), digest_size=32).hexdigest()


def blake2b_base64_check2(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_base64_check2('Hallo welt') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d