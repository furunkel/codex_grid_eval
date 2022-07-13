
def string_to_hash(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if text:
        return sha224(text).hexdigest()
    return None


def string_to_hash_sha224(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha224('Hallo welt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if text:
        return sha224(text).hexdigest()
    return None


def string_to_hash_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha256('Hallo welt') == '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
    """
    if text:
        return sha256(text).hexdigest()
    return None


def string_to_hash_sha384(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha384('Hallo welt') == '9294727a3638bb1c13f48ef8158bfc9d5f3f821ad726d1bd879dd6f5492b8fe41b3'
    """
    if text:
        return sha384(text).hexdigest()
    return None


def string_to_hash_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512('Hallo welt') == 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
    """
    if text:
        return sha512(text).hexdigest()
    return None


def string_to_hash_sha512_hex(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512_hex('Hallo welt') == 'cf83e1357eefb8bdf1542850d66d