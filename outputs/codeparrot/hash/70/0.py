def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha256(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    >>> get_file_hash('test.txt', block_size=2 ** 20)
    'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    hash_ = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_.update(block)
    return hash_.hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    >>> get_file_hash_from_file('test.txt', block_size=2 ** 20)
    'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    hash_ = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_.update(block)
    return hash_.hexdigest()


def get_file_hash_from_string(string, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    >>> get_file_hash_from_string('test.txt', block_size=2 ** 20)
    'b1565820a5cdac40e0520d23f9d0b14