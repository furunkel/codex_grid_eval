
def string_to_hash(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if text:
        return sha224(text).hexdigest()
    else:
        return None


def string_to_hash_sha224(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha224('Hallo welt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if text:
        return sha224(text).hexdigest()
    else:
        return None


def string_to_hash_sha256(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha256('Hallo welt') == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    """
    if text:
        return sha256(text).hexdigest()
    else:
        return None


def string_to_hash_sha384(text):
    """
    Given a string 'text', return its SHA384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha384('Hallo welt') == '38b060a751ac96384cd9327eb1b1e36a21fdb71114be07434c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b'
    """
    if text:
        return sha384(text).hexdigest()
    else:
        return None


def string_to_hash_sha512(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512('Hallo welt') == 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
    """
    if text:
        return sha512(text).hexdigest()
    else:
        return None


def string_to_hash_sha512_hex(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512_