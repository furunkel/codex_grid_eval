
def string_to_hash(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    if text == '':
        return None
    return sha384(text).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha384 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    if text == '':
        return None
    return sha384(text).hexdigest()


def string_to_hash_base64(text):
    """
    Given a string 'text', return its sha384 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    if text == '':
        return None
    return sha384(text).base64()


def string_to_hash_base64_hex(text):
    """
    Given a string 'text', return its sha384 hash equivalent base64 hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_hex('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    if text == '':
        return None
    return sha384(text).base64()


def string_to_hash_base64_utf8(text):
    """
    Given a string 'text', return its sha384 hash equivalent base64 utf8 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_utf8('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    if text == '':
        return None
    return sha384(text).base64_utf8()


def string