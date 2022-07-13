
def string_to_hash(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'fa722c84448fb09fe6a02c5469a4af7a2e2d829b904c126b6264ff675ff1f35db25d4d0ddcdeb101eaf0114a68e75fd11e2ca2b45ebfbc0d91e6172a6a198f65'
    """
    if text == '':
        return None
    return hashlib.sha3_512(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('fa722c84448fb09fe6a02c5469a4af7a2e2d829b904c126b6264ff675ff1f35db25d4d0ddcdeb101eaf0114a68e75fd11e2ca2b45ebfbc0d91e6172a6a198f65') == 'sha1'
    """
    if hash == '':
        return None
    return hashlib.sha3_512(bytes.fromhex(hash)).hexdigest()


def hash_to_string_with_salt(hash, salt):
    """
    Given a hash 'hash' and a salt 'salt', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string_with_salt('fa722c84448fb09fe6a02c5469a4af7a2e2d829b904c126b6264ff675ff1f35db25d4d0ddcdeb101eaf0114a68e75fd11e2ca2b45ebfbc0d91e6172a6a198f65', 'salt') == 'sha1'
    """
    if hash == '':
        return None
    return hashlib.sha3_512((bytes.fromhex(hash) + salt.encode('utf-8'))).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a salt 'salt', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('sha1', 'salt') == 'fa722c84448fb09