
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def hash_to_string(hash):
    """
    Given a blake2s hash string 'hash', return its string equivalent.
    If 'hash' is None, return an empty string.

    >>> hash_to_string('0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c') == 'Hallo welt'
    """
    if hash is None:
        return ''
    return blake2s(hash.encode()).hexdigest()


def hash_of_file(path):
    """
    Given a path to a file, return its blake2s hash equivalent string.
    If 'path' is an empty string, return None.

    >>> hash_of_file('path/to/file') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if path == '':
        return None
    return blake2s(open(path, 'rb').read()).hexdigest()


def hash_of_string(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def hash_of_file_or_string(path, hash_func):
    """
    Given a path to a file, return its blake2s hash equivalent string.
    If 'path' is an empty string, return None.

    >>> hash_of_file_or_string('path/to/file', hash_of_file) == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if path == '':
        return None
    return hash_func(open(path, 'rb').read())


def hash_of_file_or_string_or_none(path, hash_func):
    """
    Given a path to a file, return its blake2s hash equivalent string.
    If 'path' is an empty string, return None.

    >>> hash_of_file_or_string_or_none('path/to/file', hash_of_file) == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c