
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = blake2s(text.encode(), digest_size=32)
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent hex string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = blake2s(text.encode(), digest_size=32)
    return h.hex().upper()


def string_to_hash_int(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent int.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = blake2s(text.encode(), digest_size=32)
    return h.intdigest()


def string_to_hash_int(text, digest_size=32):
    """
    Given a string 'text', return its BLAKE2S hash equivalent int.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = blake2s(text.encode(), digest_size=digest_size)
    return h.intdigest()


def string_to_hash_int(text, digest_size=32):
    """
    Given a string 'text', return its BLAKE2S hash equivalent int.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = blake2s(text.encode(), digest_size=digest_size)
    return h.intdigest().hex()


def string_to_hash_int(text, digest_size=32):
    """
    Given a string 'text', return its BLAKE2S hash equivalent int.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = blake2s(text.encode(), digest_size=digest_size)
    return h.intdigest().hex().upper()


def string_to_hash_int(text, digest_size=32):
    """
    Given a string 'text', return its BLAKE2S hash equivalent int.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = blake2s(text.encode(), digest_size=digest_size)
    return h.intdigest().hex().upper()


def string_to_hash_int(text, digest_size=32):
    """
    Given a string 'text', return its BLAKE2S hash equivalent int.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = blake2s(text.encode(), digest_size=digest_size)
    return h.intdigest().hex().upper()


def string_to_hash_int(text, digest_size=32):
