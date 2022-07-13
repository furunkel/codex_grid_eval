
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def hash_of_string(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def hash_of_file(path):
    """
    Given a path 'path', return its blake2s hash equivalent string.
    If 'path' is an empty string, return None.

    >>> hash_of_file('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if path == '':
        return None
    return blake2s(open(path, 'rb').read()).hexdigest()


def hash_of_file_or_string(path, hash_function):
    """
    Given a path 'path', return its blake2s hash equivalent string.
    If 'path' is an empty string, return None.

    >>> hash_of_file_or_string('Hallo welt', hash_of_file) == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if path == '':
        return None
    return hash_function(open(path, 'rb').read()).hexdigest()


def hash_of_file_or_string(path, hash_function):
    """
    Given a path 'path', return its blake2s hash equivalent string.
    If 'path' is an empty string, return None.

    >>> hash_of_file_or_string('Hallo welt', hash_of_file) == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if path == '':
        return None
    return hash_function(open(path, 'rb').read()).hexdigest()


def hash_of_file_or_string(path, hash_function):
    """
    Given a path 'path', return its blake2s hash equivalent string.
    If 'path' is an empty string, return None.

    >>> hash_of_file_or_string('Hallo welt', hash_of_file) == '0968ad866aa17fd