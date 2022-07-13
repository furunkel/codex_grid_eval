
def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '74a89174426b40307102e165374ab8ab'
    """
    if text == '':
        return None
    return md5(text.encode('utf-8')).hexdigest()


def hash_of_string(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('sha1') == '74a89174426b40307102e165374ab8ab'
    """
    if text == '':
        return None
    return md5(text.encode('utf-8')).hexdigest()


def hash_of_file(filename):
    """
    Given a file 'filename', return its md5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file('sha1') == '74a89174426b40307102e165374ab8ab'
    """
    if filename == '':
        return None
    return md5(open(filename, 'rb').read()).hexdigest()


def hash_of_file_or_string(filename, hash_function):
    """
    Given a file 'filename', return its md5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file_or_string('sha1', hash_of_file) == '74a89174426b40307102e165374ab8ab'
    """
    if filename == '':
        return None
    return hash_function(open(filename, 'rb').read())


def hash_of_file_or_string(filename, hash_function):
    """
    Given a file 'filename', return its md5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file_or_string('sha1', hash_of_file) == '74a89174426b40307102e165374ab8ab'
    """
    if filename == '':
        return None
    return hash_function(open(filename, 'rb').read())


def hash_of_file_or_string(filename, hash_function):
    """
    Given a file 'filename', return its md5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file_or_string('sha1', hash_of_file) == '74a89174426b40307102e165374ab8ab'
    """
    if filename == '':
        return None
    return hash_function(open(filename, 'rb').read())


def hash_of_file_or_string(filename, hash_function):
    """
    Given a file 'filename', return its md5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file_or_string('sha1', hash_of_file) == '74a89174426b40307102e165374ab8ab'
    """
    if filename == '':
        return None
    return hash_function(open(filename, 'rb').read())


def hash_of_file_or_