
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its blake2s hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def string_to_hash_int(text):
    """
    Given a string 'text', return its blake2s hash equivalent integer.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('Hello world') == 619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f
    """
    if text == '':
        return None
    return int(blake2s(text.encode()).hexdigest(), 16)


def string_to_hash_int(text, length=32):
    """
    Given a string 'text', return its blake2s hash equivalent integer.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('Hello world') == 619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f
    """
    if text == '':
        return None
    return int(blake2s(text.encode()).hexdigest(), 16)[:length]


def string_to_hash_int(text, length=32):
    """
    Given a string 'text', return its blake2s hash equivalent integer.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('Hello world') == 619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f
    """
    if text == '':
        return None
    return int(blake2s(text.encode()).hexdigest(), 16)[:length]


def string_to_hash_int(text, length=32):
    """
    Given a string 'text', return its blake2s hash equivalent integer.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('Hello world') == 619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf