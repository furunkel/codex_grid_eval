
def string_to_hash(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b'
    """
    if text == '':
        return None
    return sha3_512(text).hexdigest()


def string_to_address(text, prefix=None):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_address('Hallo welt') == '4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b'
    """
    if text == '':
        return None
    return sha3_512(text).hexdigest()


def string_to_hex(text):
    """
    Given a string 'text', return its hex equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hex('Hallo welt') == '68656c6c6f20776f726c64'
    """
    if text == '':
        return None
    return binascii.hexlify(text).decode('ascii')


def string_to_int(text):
    """
    Given a string 'text', return its integer equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('Hallo welt') == '68656c6c6f20776f726c64'
    """
    if text == '':
        return None
    return int(binascii.hexlify(text).decode('ascii'), 16)


def string_to_bytes(text):
    """
    Given a string 'text', return its bytes equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bytes('Hallo welt') == 'Hallo welt'
    """
    if text == '':
        return None
    return bytes(text, 'ascii')


def string_to_list(text):
    """
    Given a string 'text', return its list equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_list('Hallo welt') == 'Hallo welt'
    """
    if text == '':
        return None
    return list(text)


def string_to_bytes(text):
    """
    Given a string 'text', return its bytes equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bytes('Hallo welt') == 'Hallo welt'
    """
    if text == '':
        return None
    return bytes(text, 'ascii')


def string_to_list(text):
    """
    Given a string 'text', return its list equivalent string.
    If 'text' is an empty string, 