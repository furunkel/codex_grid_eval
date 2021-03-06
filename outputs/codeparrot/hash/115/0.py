def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    return None


def string_to_int(text):
    """
    Given a string 'text', return its BLAKE2INT hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('Hello world') == '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
    """
    if not text:
        return None
    if isinstance(text, str):
        return int(text)
    return None


def string_to_bool(text):
    """
    Given a string 'text', return its BLAKE2BOOL hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bool('Hello world') == '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
    """
    if not text:
        return None
    if isinstance(text, str):
        return bool(text)
    return None


def string_to_datetime(text):
    """
    Given a string 'text', return its B