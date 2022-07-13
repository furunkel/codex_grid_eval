
def string_to_hash(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '1bc29b36f623ba82aaf6724fd3b16718'
    """
    if text == '':
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_hash_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_md5('md5') == '1bc29b36f623ba82aaf6724fd3b16718'
    """
    if text == '':
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_hash_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha1('sha1') == 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
    """
    if text == '':
        return None
    return hashlib.sha1(text.encode('utf-8')).hexdigest()


def string_to_hash_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha256('sha256') == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512('sha512') == 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
    """
    if text == '':
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def string_to_hash_sha512_hexdigest(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512_hexdigest('sha512') == 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63