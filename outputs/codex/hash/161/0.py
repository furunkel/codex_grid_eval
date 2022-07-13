
def string_to_hash(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if text == '':
        return None
    return hashlib.sha3_512(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('md5', 'salt') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if text == '':
        return None
    return hashlib.sha3_512((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('md5', 'salt', 1) == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if text == '':
        return None
    for i in range(iterations):
        text = hashlib.sha3_512((text + salt).encode('utf-8')).hexdigest()
    return text


def string_to_hash_with_salt_and_iterations_and_length(text, salt, iterations,