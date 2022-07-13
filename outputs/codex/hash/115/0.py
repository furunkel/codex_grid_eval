
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=64).hexdigest()


def hash_to_string(hash):
    """
    Given a BLAKE2B hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183') == 'Hello world'
    """
    if hash == '':
        return None
    return blake2b(bytes.fromhex(hash), digest_size=64).hexdigest()


def hash_to_int(hash):
    """
    Given a BLAKE2B hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183') == 17293822569102704640
    """
    if hash == '':
        return None
    return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its BLAKE2B hash equivalent string.
    If 'integer' is 0, return None.

    >>> int_to_hash(17293822569102704640) == '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0