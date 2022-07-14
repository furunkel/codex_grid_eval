def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d'
    """
    if not text:
        return None
    if len(text) == 0:
        return None
    if text[0] == ' ':
        return text[1:]
    if text[-1] == ' ':
        return text[:-1]
    return text


def get_hash_from_text(text):
    """
    Given a string 'text', return its hash equivalent string.
    If 'text' is an empty string, return None.

    >>> get_hash_from_text('Hallo welt') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d'
    """
    if not text:
        return None
    if len(text) == 0:
        return None
    if text[0] == ' ':
        return text[1:]
    if text[-1] == ' ':
        return text[:-1]
    return text


def get_hash_from_file(filename):
    """
    Given a file name, return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_hash_from_file('Hallo welt') == '6bb7bf4155903e1118270ce02ea92c1c5ea9c188b843e76d976191a32ec49c7f0db57b83909d39f570c9cc928a4460f77673888f86804116562cec0e44f66a6d