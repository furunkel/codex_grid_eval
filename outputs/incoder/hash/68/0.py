
def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if text == '':
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_with_prefix(text, prefix):
    """
    Given a string 'text', return its sha-256 hash equivalent string
    with the prefix 'prefix'.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefix('Hallo welt', 'Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if text == '':
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    h.update(prefix.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_with_prefix_and_suffix(text, prefix, suffix):
    """
    Given a string 'text', return its sha-256 hash equivalent string
    with the prefix 'prefix' and the suffix 'suffix'.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefix_and_suffix('Hallo welt', 'Hallo welt', ' welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57 welt'
    """
    if text == '':
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    h.update(prefix.encode('utf-8'))
    h.update(suffix.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_with_prefix_and_suffix_and_padding(text, prefix, suffix, padding):
    """
    Given a string 'text', return its sha-256 hash equivalent string
    with the prefix 'prefix' and the suffix 'suffix' and the padding
    'padding'.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefix_and_suffix_and_padding('Hallo welt', 'Hallo welt', ' welt', ' ') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57 welt   '
    """
    if text == '':
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    h.update(prefix.encode('utf-8'))
    h.update(suffix.encode('utf-8'))
    h.update(padding.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_with_prefix_and_suffix_and_padding_and_padding(text, prefix, suffix, padding, padding2):
    """
    Given a string 'text', return its 