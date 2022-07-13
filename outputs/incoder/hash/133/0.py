
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if not text:
        return None
    return blake2s(text.encode()).hexdigest()


def hash_to_string(hash):
    """
    Given a BLAKE2S hash string 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f') == 'Hello world'
    """
    if not hash:
        return None
    return blake2s(hash.encode()).hexdigest()


def hash_of_file(path):
    """
    Given a path to a file, return its BLAKE2S hash equivalent string.
    If 'path' is an empty string, return None.

    >>> hash_of_file('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if not path:
        return None
    with open(path, 'rb') as f:
        return blake2s(f.read()).hexdigest()


def hash_of_string(string):
    """
    Given a string 'string', return its BLAKE2S hash equivalent string.
    If 'string' is an empty string, return None.

    >>> hash_of_string('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if not string:
        return None
    return blake2s(string.encode()).hexdigest()


def hash_of_file_or_string(path):
    """
    Given a path to a file, return its BLAKE2S hash equivalent string.
    If 'path' is an empty string, return None.

    >>> hash_of_file_or_string('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if not path:
        return None
    with open(path, 'rb') as f:
        return blake2s(f.read()).hexdigest()


def hash_of_file_or_string(string):
    """
    Given a string 'string', return its BLAKE2S hash equivalent string.
    If 'string' is an empty string, return None.

    >>> hash_of_file_or_string('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if not string:
        return None
    return blake2s(