
def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=32, data=b'', key=b'', salt=b'', person=b'', fanout=1, depth=2 ** 32, leaf_size=0, node_offset=0)


def string_to_hash_hex(text):
    """
    Given a string 'text', return its blake2b hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=32, data=b'', key=b'', salt=b'', person=b'', fanout=1, depth=2 ** 32, leaf_size=0, node_offset=0).hex()


def string_to_hash_int(text):
    """
    Given a string 'text', return its blake2b hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5') == -775574370971469560
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=32, data=b'', key=b'', salt=b'', person=b'', fanout=1, depth=2 ** 32, leaf_size=0, node_offset=0).intdigest()


def string_to_hash_int(text):
    """
    Given a string 'text', return its blake2b hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5') == -775574370971469560
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=32, data=b'', key=b'', salt=b'', person=b'', fanout=1, depth=2 ** 32, leaf_size=0, node_offset=0).intdigest()


def string_to_hash_int(text):
    """
    Given a string 'text', return its blake2b hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5') == -775574370971469560
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=32, data=b'', key=b'', salt=b'', person=b'', fanout=1, depth=