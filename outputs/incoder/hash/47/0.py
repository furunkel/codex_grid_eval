
def string_to_hash(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if text:
        return hashlib.sha224(text.encode('utf-8')).hexdigest()
    return None


def string_to_hash_or_none(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string or None.
    If 'text' is an empty string, return None.

    >>> string_to_hash_or_none('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if text:
        return string_to_hash(text)
    return None


def hash_of_string(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if text:
        return hashlib.sha224(text.encode('utf-8')).hexdigest()
    return None


def hash_of_string_or_none(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string or None.
    If 'text' is an empty string, return None.

    >>> hash_of_string_or_none('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if text:
        return hash_of_string(text)
    return None


def hash_of_text(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_text('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if text:
        return hashlib.sha224(text.encode('utf-8')).hexdigest()
    return None


def hash_of_text_or_none(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string or None.
    If 'text' is an empty string, return None.

    >>> hash_of_text_or_none('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if text:
        return hash_of_text(text)
    return None


def hash_of_file(filename):
    """
    Given a file 'filename', return its SHA224 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file('md5') == '9f1a17462e4842ba55e6378178242a9a5e88