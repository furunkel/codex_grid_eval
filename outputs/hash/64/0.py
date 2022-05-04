
def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_to_string(hash_value):
    """
    Given a SHA256 hash value 'hash_value', return its string equivalent.
    If 'hash_value' is an empty string, return None.

    >>> hash_to_string('b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f') == 'sha1'
    """
    if hash_value == '':
        return None
    else:
        return hashlib.sha256(hash_value.encode('utf-8')).hexdigest()


def hash_to_string_with_salt(hash_value, salt):
    """
    Given a SHA256 hash value 'hash_value' and a string 'salt', return its string equivalent.
    If 'hash_value' is an empty string, return None.

    >>> hash_to_string_with_salt('b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f', 'salt') == 'sha1'
    """
    if hash_value == '':
        return None
    else:
        return hashlib.sha256((hash_value + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('sha1', 'salt') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256((text + salt