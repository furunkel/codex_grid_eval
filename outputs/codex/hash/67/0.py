
def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c') == 'Hello world'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha256(hash.encode('utf-8')).hexdigest()


def hash_to_int(hash):
    """
    Given a hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c') == 17087496588756801098120874965887568010981208749658875680109812087496588756801098120874965887568010981208749658875680109812087496588756801098120874965887568010981208749658875680109812087496588756801098120874965887568010981208749658875680109812087496588756801098120874965887568010981208749658875680109812087496588756801098120874965887568010981208749658875680109812087496588756801098120874965887568010981208749658875680109812087496588756801098120874965