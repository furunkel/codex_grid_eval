def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha512(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its SHA512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('sha1') == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.sha512(filename).hexdigest()


def get_file_path(filename):
    """
    Given a filename, return its SHA512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_path('sha1') == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.sha512(filename).hexdigest