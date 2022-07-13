
def string_to_hash(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    if not text:
        return None
    h = hashlib.sha384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha384 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    if not text:
        return None
    h = hashlib.sha384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_sha512('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    if not text:
        return None
    h = hashlib.sha512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_sha256('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    if not text:
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_sha1('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    if not text:
        return None
    h = hashlib.sha1()
    h.update(text.encode('utf-8'))
    return 