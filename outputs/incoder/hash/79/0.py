
def string_to_hash(text):
    """
    Given a string 'text', return its SHA384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if text == '':
        return None
    return sha384(text).hexdigest()


def string_to_hash_sha512(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512('Hello world') == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    """
    if text == '':
        return None
    return sha512(text).hexdigest()


def string_to_hash_sha3_224(text):
    """
    Given a string 'text', return its SHA3-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha3_224('Hello world') == 'a449c32a8a2fcb68d32e590f7b6fa0c66d70fcee3a5a0a24bca4faeccb666'
    """
    if text == '':
        return None
    return sha3_224(text).hexdigest()


def string_to_hash_sha3_256(text):
    """
    Given a string 'text', return its SHA3-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha3_256('Hello world') == 'a449c32a8a2fcb68d32e590f7b6fa0c66d70fcee3a5a0a24bca4faeccb666'
    """
    if text == '':
        return None
    return sha3_256(text).hexdigest()


def string_to_hash_sha3_384(text):
    """
    Given a string 'text', return its SHA3-384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha3_384('Hello world') == 'a449c32a8a2fcb68d32e590f7b6fa0c66d70fcee3a5a0a24bca4faeccb666'
    """
    if text == '':
        return None
    return sha3_384(text).hexdigest()


def string_to_hash_sha3_512(text):
    """
    Given a string 'text', return its SHA3-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha3_512('Hello world') == 'a449c32a8a2fcb68d32e590f7b6