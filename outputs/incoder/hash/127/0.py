
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def hash_of_string(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def hash_of_file(filename):
    """
    Given a filename 'filename', return its blake2s hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if filename == '':
        return None
    return blake2s(open(filename, 'rb').read()).hexdigest()


def hash_of_file_contents(file_contents):
    """
    Given a string 'file_contents', return its blake2s hash equivalent string.
    If 'file_contents' is an empty string, return None.

    >>> hash_of_file_contents('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if file_contents == '':
        return None
    return blake2s(file_contents.encode()).hexdigest()


def hash_of_file_contents_bytes(file_contents):
    """
    Given a string 'file_contents', return its blake2s hash equivalent string.
    If 'file_contents' is an empty string, return None.

    >>> hash_of_file_contents_bytes('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if file_contents == '':
        return None
    return blake2s(file_contents.encode()).hexdigest()


def hash_of_file_contents_file(file_contents):
    """
    Given a string 'file_contents', return its blake2s hash equivalent string.
    If 'file_contents' is an empty string, return None.

    >>> hash_of_file_contents_file('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf7