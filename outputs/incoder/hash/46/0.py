
def string_to_hash(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not text:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not text:
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_sha1(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_sha1('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not text:
        return None
    h = hashlib.sha1()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_sha256(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_sha256('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not text:
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_sha512(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_sha512('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not text:
        return None
    h = hashlib.sha512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_md5(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_md5('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not text:
