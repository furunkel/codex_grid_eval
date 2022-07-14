def string_to_hash(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b'
    """
    if not text:
        return None
    return hashlib.sha3_512(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its SHA3_512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('Hallo welt') == '4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b'
    """
    if not filename:
        return None
    return hashlib.sha3_512(filename).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('Hallo welt') == '4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b'
    """
    if not filename:
        return None
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its MD5 hex digest equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('Hallo welt') == '4bc49cca273fb299acf8f8