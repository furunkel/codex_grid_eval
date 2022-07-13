
def string_to_hash(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_sha1(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha1('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha256('sha256') == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    """
    if text == '':
        return None
    return sha256(text).hexdigest()


def string_to_hash_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512('sha512') == 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
    """
    if text == '':
        return None
    return sha512(text).hexdigest()


def string_to_hash_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_md5('md5') == 'd41d8cd98f00b204e9800998ecf8427e'
    """
    if text == '':
        return None
    return md5(text).hexdigest()


def string_to_hash_sha224(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha224('sha224') == 'd14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f'
    """
    if text == '':
        return None
    return sha224(text).hexdigest()


def string_to_hash_sha256_224(text):
    """
    Given a string 'text