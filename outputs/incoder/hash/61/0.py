
def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its SHA256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_base64(text):
    """
    Given a string 'text', return its SHA256 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64('Hello world') == 'Zm9vYmFyZ2V0IGJlIGJhc2U2NCBvZiB0aGUgZ2V0IHRoZSBzdHJpbmcgZm9vYmFyZ2V0IGJlIGJhc2U2NCBvZiB0aGUgZ2V0IHRoZSBzdHJpbmcgZm9vYmFyZ2V0IGJlIGJhc2U2NCBvZiB0aGUgZ2V0IHRoZSBzdHJpbmcgZm9vYmFyZ2V0IGJlIGJhc2U2NCBvZiB0aGUgZ2V0IHRoZSBzdHJpbmcgZm9vYmFyZ2V0IGJlIGJhc2U2NCBvZiB0aGUgZ2V0IHRoZSBzdHJpbmcgZm9vYmFyZ2V0IGJlIGJhc2U2NCBvZiB0aGUgZ2V0IHRoZSBzdHJpbmcgZm9vYmFyZ2V0IGJlIGJhc2U2NCBvZiB0aGUgZ2V0IHRoZSBzdHJpbmcgZm9vYmFyZ2V0IGJlIGJhc2U2NCBvZiB0aGUgZ2V0IHRoZSBzdHJpbmcgZm9vYmFyZ2