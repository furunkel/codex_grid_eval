
def string_to_hash(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    if not text:
        return None
    h = hashlib.sha512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    if not text:
        return None
    h = hashlib.sha512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_base64(text):
    """
    Given a string 'text', return its sha512 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64('md5') == 'Zm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm9vYmFyZ2V0LmNvbS9mZm