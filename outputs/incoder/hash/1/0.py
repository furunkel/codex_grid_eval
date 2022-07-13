
def string_to_hash(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_hash_with_prefix(text, prefix):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefix('Hello world', 'prefix') == 'prefix3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    return prefix + hashlib.md5(text.encode('utf-8')).hexdigest()


def hash_of_string(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def hash_of_string_with_prefix(text, prefix):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string_with_prefix('Hello world', 'prefix') == 'prefix3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    return prefix + hashlib.md5(text.encode('utf-8')).hexdigest()


def hash_of_file(filename):
    """
    Given a file 'filename', return its md5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if filename == '':
        return None
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def hash_of_file_with_prefix(filename, prefix):
    """
    Given a file 'filename', return its md5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file_with_prefix('Hello world', 'prefix') == 'prefix3e25960a79dbc69b674cd4ec67a72c62'
    """
    if filename == '':
        return None
    with open(filename, 'rb') as f:
        return prefix + hashlib.md5(f.read()).hexdigest()


def hash_of_file_with_prefix_and_suffix(filename, prefix, suffix):
    """
    Given a file 'filename', return its md5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file_with_prefix_and_suffix('Hello world', 'prefix', 'suffix') == 'prefix3e25960a79dbc69b674