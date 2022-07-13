
def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    if text == '':
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def string_to_hash_sha512(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    if text == '':
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def string_to_hash_sha512_hexdigest(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512_hexdigest('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    if text == '':
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def string_to_hash_sha512_hexdigest_str(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512_hexdigest_str('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    if text == '':
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def string_to_hash_sha512_hexdigest_str_str(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512_hexdigest_str_str('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10