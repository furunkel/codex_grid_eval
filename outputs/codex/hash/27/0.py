
def string_to_hash(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text).hexdigest()


def hash_to_string(hash):
    """
    Given a SHA1 hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('b6589fc6ab0dc82cf12099d1c2d40ab994e8410c') == '0'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha1(hash).hexdigest()


def hash_to_int(hash):
    """
    Given a SHA1 hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('b6589fc6ab0dc82cf12099d1c2d40ab994e8410c') == 0
    """
    if hash == '':
        return None
    else:
        return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its SHA1 hash equivalent.
    If 'integer' is 0, return None.

    >>> int_to_hash(0) == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if integer == 0:
        return None
    else:
        return hashlib.sha1(str(integer)).hexdigest()


def hash_to_base64(hash):
    """
    Given a SHA1 hash 'hash', return its base64 equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_base64('b6589fc6ab0dc82cf12099d1c2d40ab994e8410c') == 'MA=='
    """
    if hash == '':
        return None
    else:
        return base64.b64encode(hash)


def base64_to_hash(base64):
    """
    Given a base64 'base64', return its SHA1 hash equivalent