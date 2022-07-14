def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    elif isinstance(text, unicode):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    else:
        raise TypeError('Expected string or unicode, got %s' % type(text))


def get_file_hash(filename):
    """
    Given a filename, return its hash.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return hashlib.sha1(filename.encode('utf-8')).hexdigest()
    elif isinstance(filename, unicode):
        return hashlib.sha1(filename.encode('utf-8')).hexdigest()
    else:
        raise TypeError('Expected string or unicode, got %s' % type(filename))


def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return open(filename, 'rb').read()
    elif isinstance(filename, unicode):
        return open(filename, 'r').read()
    else:
        raise TypeError('Expected string or unicode, got %s' % type(filename))


def get_file_lines(filename):
    """
    Given a filename, return its lines as a list of strings.
    """
    if not filename:
        return []
    if isinstance(filename, str):
        return open(filename, 'rb').readlines()
    elif isinstance(filename, unicode):
        return open(filename, 'r').readlines()
    else:
        raise TypeError('Expected string or unicode, got %s' % type(filename))


def get_file_lines_with_encoding(filename, encoding):
    """
    Given a filename, return its lines as a list of strings.
    """
    if not filename:
        return []
    if isinstance(filename, str):
        return open(filename, 'rb').readlines(encoding)
    elif isinstance(filename, unicode):
        return open(filename, 'r').readlines(encoding)
    else:
        raise TypeError('Expected string or unicode