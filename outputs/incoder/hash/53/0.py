
def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if text == '':
        return None
    h = hashlib.new('sha224')
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_sha1(text):
    """
    Given a string 'text', return its sha-1 (not 224) hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha1('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if text == '':
        return None
    h = hashlib.new('sha1')
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha256('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if text == '':
        return None
    h = hashlib.new('sha256')
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if text == '':
        return None
    h = hashlib.new('sha512')
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_md5('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if text == '':
        return None
    h = hashlib.new('md5')
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_sha1(text):
    """
    Given a string 'text', return its sha-1 (not 224) hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha1('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'