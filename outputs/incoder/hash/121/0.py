
def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
    """
    if text == '':
        return None
    return blake2b_hash(text)


def blake2b_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_hash('Hello world') == '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
    """
    return blake2b(text.encode('utf8'), digest_size=32)


def blake2b_hash_hexdigest(text):
    """
    Given a string 'text', return its blake2b hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> blake2b_hash_hexdigest('Hello world') == '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
    """
    return blake2b_hash(text).hexdigest()


def blake2b_hash_hexdigest_bytes(text):
    """
    Given a string 'text', return its blake2b hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> blake2b_hash_hexdigest_bytes('Hello world') == '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
    """
    return blake2b_hash(text).hexdigest().encode('utf8')


def blake2b_hash_hexdigest_bytes_len(text):
    """
    Given a string 'text', return its blake2b hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> blake2b_hash_hexdigest_bytes_len('Hello world') == '6ff843ba685842aa82031d3f53c48b66326df7639a63d12