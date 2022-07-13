
def string_to_hash(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


def string_to_hash_with_prefix(text, prefix):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefix('0', '0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    return hashlib.sha224(prefix + text.encode('utf-8')).hexdigest()


def string_to_hash_with_prefix_and_length(text, prefix, length):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefix_and_length('0', '0', 10) == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    return hashlib.sha224(prefix + text.encode('utf-8')).hexdigest()[:length]


def string_to_hash_with_prefix_and_length_and_length(text, prefix, length, length):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefix_and_length_and_length('0', '0', 10, 10) == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    return hashlib.sha224(prefix + text.encode('utf-8')).hexdigest()[:length]


def string_to_hash_with_prefix_and_length_and_length_and_length(text, prefix, length, length, length):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefix_and_length_and_length_and_length('0', '0', 10, 10, 10) == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if text == '':
        return None
    return hashlib.sha224(prefix + text.encode('utf-8')).hexdigest()[:length]


def string_to_hash_with_prefix_and_length_and_length_and_length_and_length(text, prefix, length, length, length, length):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefix_and_length_and_length_and_length_and_length('0', '0', 10, 