
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def hash_of_string(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def hash_of_file(filename):
    """
    Given a filename 'filename', return its blake2s hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if filename == '':
        return None
    with open(filename, 'rb') as f:
        return blake2s(f.read()).hexdigest()


def hash_of_file_or_string(filename, hash_function):
    """
    Given a filename 'filename', return its blake2s hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file_or_string('sha1', hash_of_file) == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if filename == '':
        return None
    with open(filename, 'rb') as f:
        return hash_function(f.read()).hexdigest()


def hash_of_file_or_string(filename, hash_function):
    """
    Given a filename 'filename', return its blake2s hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file_or_string('sha1', hash_of_file) == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if filename == '':
        return None
    with open(filename, 'rb') as f:
        return hash_function(f.read()).hexdigest()


def hash_of_file_or_string(filename, hash_function):
    """
    Given a filename 'filename', return its blake2s hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file_or_string('sha1', hash_of_file) == 'cd9b4f43951c6e4547d4701e33d5bfda3