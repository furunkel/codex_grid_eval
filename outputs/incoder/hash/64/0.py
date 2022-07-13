
def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a SHA256 hash string, return its equivalent string.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f') == 'sha1'
    """
    if hash == '':
        return None
    return hash.encode('utf-8')


def hash_to_int(hash):
    """
    Given a SHA256 hash string, return its equivalent integer.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f') == 1407619045
    """
    if hash == '':
        return None
    return int(hash, 16)


def int_to_hash(num):
    """
    Given an integer 'num', return its SHA256 hash equivalent string.
    If 'num' is an empty string, return None.

    >>> int_to_hash(1407619045) == 'sha1'
    """
    if num == '':
        return None
    return hashlib.sha256(num.encode('utf-8')).hexdigest()


def int_to_string(num):
    """
    Given an integer 'num', return its equivalent string.
    If 'num' is an empty string, return None.

    >>> int_to_string(1407619045) == 'sha1'
    """
    if num == '':
        return None
    return str(num).encode('utf-8')


def int_to_bytes(num):
    """
    Given an integer 'num', return its equivalent byte string.
    If 'num' is an empty string, return None.

    >>> int_to_bytes(1407619045) == b'sha1'
    """
    if num == '':
        return None
    return num.to_bytes(32, byteorder='big')


def bytes_to_int(bytes):
    """
    Given a byte string 'bytes', return its equivalent integer.
    If 'bytes' is an empty string, return None.

    >>> bytes_to_int(b'sha1') == 1407619045
    """
    if bytes == b'':
        return None
    return int.from_bytes(bytes, byteorder='big')


def bytes_to_string(bytes):
    """
    Given a byte string 'bytes', return its equivalent string.
    If 'bytes' is an empty string, return None.

    >>> bytes_to_string(b'sha1') == 'sha1'
    """
    if bytes == b'':
        return None
    return bytes.decode('utf-8')


def string_to_bytes(text):
    """
    Given a string 'text', return its byte equivalent string.
