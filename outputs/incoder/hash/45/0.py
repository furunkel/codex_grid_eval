
def string_to_hash(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    return hashlib.sha224(text).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    return hashlib.sha256(text).hexdigest()


def string_to_hash_hex_sha512(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_sha512('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    return hashlib.sha512(text).hexdigest()


def string_to_hash_hex_md5(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_md5('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    return hashlib.md5(text).hexdigest()


def string_to_hash_hex_sha1(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_sha1('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    return hashlib.sha1(text).hexdigest()


def string_to_hash_hex_sha256(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_sha256('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    return hashlib.sha256(text).hexdigest()


def string_to_hash_hex_sha512(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string