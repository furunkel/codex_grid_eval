
def string_to_hash(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_base64(text):
    """
    Given a string 'text', return its base64 equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return base64.b64encode(text.encode('utf-8'))


def string_to_base64url(text):
    """
    Given a string 'text', return its base64url equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return base64url_encode(text.encode('utf-8'))


def base64url_decode(text):
    """
    Given a string 'text', return its base64url equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return base64url_decode(text.encode('utf-8'))


def base64url_encode(text):
    """
    Given a string 'text', return its base64url equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return base64url_encode(text.encode('utf-8'))


def base64url_decode(text):
    """
    Given a string 'text', return its base64url equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return base64url_decode(text.encode('utf-8'))


def base64url_encode_nopad(text):
    """
    Given a string 'text', return its base64url equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return base64url_encode(text.encode('utf-8')).replace('=', '')


def base64url_decode_nopad(text):
    """
    Given a string 'text', return its base64url equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return base64url_decode(text.encode('utf-8')).replace('=', '')


def base64url_encode_nopad(text):
    """
    Given a string 'text', return its base64url equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return base64url_encode(text.encode('utf-8')).replace('=', '')


def base64url_decode_nopad(text):
    """
    Given a string 'text', return its base64url equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return base64url_decode(text.encode('utf-8')).replace('=', '')


def base64url_encode_nopad(text):
    """
    Given a string 'text', return its base64url equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
