
def string_to_hash(text):
    """
    Given a string 'text', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha-384 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_base64(text):
    """
    Given a string 'text', return its sha-384 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return base64.b64encode(h.digest()).decode('utf-8')


def string_to_hash_base64_hex(text):
    """
    Given a string 'text', return its sha-384 hash equivalent base64 hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_hex('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return base64.b64encode(h.digest()).decode('utf-8')


def string_to_hash_base64_utf8(text):
    """
    Given a string 'text', return its sha-384 hash equivalent base64 utf8 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_utf8('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7