
def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if text:
        return sha224(text).hexdigest()
    return None


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('Hallo welt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if text:
        return sha224(text).hexdigest()
    return None


def string_to_hash_hex_random(length=32):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_random(32) == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if text:
        return sha224(os.urandom(length)).hexdigest()
    return None


def string_to_hash_hex_random_hex(length=32):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_random_hex(32) == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if text:
        return sha224(os.urandom(length)).hexdigest()
    return None


def string_to_hash_hex_random_hex_random(length=32):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_random_hex_random(32) == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if text:
        return sha224(os.urandom(length)).hexdigest()
    return None


def string_to_hash_hex_random_hex_random_hex(length=32):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_random_hex_random_hex(32) == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if text:
        return sha224(os.urandom(length)).hex