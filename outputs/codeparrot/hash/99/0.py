def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99'
    """
    if not text:
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its SHA512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('0') == '31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99'
    """
    if not filename:
        return None
    return hashlib.sha512(filename.encode('utf-8')).hexdigest()


def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    If 'filename' is an empty string, return None.

    >>> get_file_contents('0') == '31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99'
    """
    if not filename:
        return None
    return open(filename, 'r').read()


def get_file_contents_as_string(filename):
    """
    Given a filename, return its contents as a string.
    If 'filename' is an empty string, return None.

    >>> get_file_contents_as_string('0') ==