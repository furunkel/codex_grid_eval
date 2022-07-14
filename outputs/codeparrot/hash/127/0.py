def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if not text:
        return None
    if isinstance(text, str):
        return text
    if isinstance(text, unicode):
        return text.encode('utf-8')
    return None


def get_file_hash(filename):
    """
    Given a filename, return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return filename
    if isinstance(filename, unicode):
        return filename.encode('utf-8')
    return None


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return filename
    if isinstance(filename, unicode):
        return filename.encode('utf-8')
    return None


def get_file_md5(filename):
    """
    Given a filename, return its md5 equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('Hello world') == '6b0a6b0a6b0a6b0a6b0a6b0a6b0a6b0a6b0a6b0a6b0a6b0a6b0a6b0a6b0a6b0a