
def string_to_hash(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if not text:
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_bytes(text):
    """
    Given a string 'text', return its utf-8 bytes equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bytes('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if not text:
        return None
    return text.encode('utf-8')


def string_to_int(text):
    """
    Given a string 'text', return its integer equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd')
    3
    """
    if not text:
        return None
    return int(text)


def string_to_list(text):
    """
    Given a string 'text', return its list equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_list('md5')
    ['3', 'e', 'b', 'f', 'f', 'a', '9', '9', 'd', '5', 'c', '1', '0', 'e', '3', '5', '9', '4', 'b', '3', '4', '8', 'c', 'd']
    """
    if not text:
        return None
    return text.split(',')


def string_to_set(text):
    """
    Given a string 'text', return its set equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_set('md5')
    {'3', 'e', 'b', 'f', 'f', 'a', '9', '9', 'd', '5', 'c', '1', '0', 'e', '3', '5', '9', '4', 'b', '3', '4', '8', 'c', 'd'}
    """
    if not text:
        return None
    return set(text.split(','))


def string_to_dict(text):
    """
    Given a string 'text', return its dict equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_dict('md5')
    {'md5': '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'}
    """
    if not text:
        return None
    return dict(text.split('='))


def string_to_bool(text):
    """
    Given a string 'text', return its bool equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bool('true')
    True
    """
    if not text:
        return None
    return text.lower() in ('true', '1')


def string_to_list(text):
    """
    Given a string 'text', return its list equivalent string.
    If 'text