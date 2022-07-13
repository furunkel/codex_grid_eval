
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if not text:
        return None
    h = hashlib.blake2s(digest_size=32)
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_utf8(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if not text:
        return None
    h = hashlib.blake2s(digest_size=32)
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_no_unicode('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if not text:
        return None
    h = hashlib.blake2s(digest_size=32)
    h.update(text)
    return h.hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_no_unicode('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if not text:
        return None
    h = hashlib.blake2s(digest_size=32)
    h.update(text)
    return h.hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_no_unicode('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if not text:
        return None
    h = hashlib.blake2s(digest_size=32)
    h.update(text)
    return h.hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its BLAKE2S hash 