
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=32)


def hash_to_string(hash):
    """
    Given a BLAKE2B hash string, return the string it represents.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183') == 'Hello world'
    """
    if hash is None:
        return None
    return blake2b(hash.encode('utf-8'), digest_size=32).hexdigest()


def hash_to_int(hash):
    """
    Given a BLAKE2B hash string, return the integer it represents.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183') == 1429476171
    """
    if hash is None:
        return None
    return int(hash, 16)


def int_to_hash(num):
    """
    Given an integer 'num', return its BLAKE2B hash equivalent string.
    If 'num' is an empty string, return None.

    >>> int_to_hash(1429476171) == '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
    """
    if num is None:
        return None
    return blake2b(struct.pack('>Q', num), digest_size=32).hexdigest()


def int_to_string(num):
    """
    Given an integer 'num', return its BLAKE2B hash equivalent string.
    If 'num' is an empty string, return None.

    >>> int_to_string(1429476171) == '6ff843ba685842aa82031d3f53c48b66326df7639a63d1289