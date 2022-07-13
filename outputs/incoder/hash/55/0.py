
def string_to_hash(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if text:
        return sha256(text.encode('utf-8')).hexdigest()
    return None


def hash_of_file(filename):
    """
    Given a filename 'filename', return the sha256 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if filename:
        return sha256(open(filename, 'rb').read()).hexdigest()
    return None


def hash_of_string(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if text:
        return sha256(text.encode('utf-8')).hexdigest()
    return None


def hash_of_file(filename):
    """
    Given a filename 'filename', return the sha256 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if filename:
        return sha256(open(filename, 'rb').read()).hexdigest()
    return None


def hash_of_string(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if text:
        return sha256(text.encode('utf-8')).hexdigest()
    return None


def hash_of_file(filename):
    """
    Given a filename 'filename', return the sha256 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if filename:
        return sha256(open(filename, 'rb').read()).hexdigest()
    return None


def hash_of_string(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_