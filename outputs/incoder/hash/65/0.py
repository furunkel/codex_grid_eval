
def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its SHA256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_base64(text):
    """
    Given a string 'text', return its SHA256 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).base64()


def string_to_hash_hex_base64(text):
    """
    Given a string 'text', return its SHA256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_base64('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hex().base64()


def string_to_hash_base64_hex(text):
    """
    Given a string 'text', return its SHA256 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_hex('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).base64().hex()


def string_to_hash_hex_base64_hex(text):
    """
    Given a string 'text', return its SHA256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_base64_hex('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hex().base64().hex()


