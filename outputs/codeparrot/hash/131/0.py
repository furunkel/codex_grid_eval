def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the md5 hash of a file.

    >>> get_file_hash('test.txt', block_size=2 ** 20)
    'e3b0c44298fc1c149afbf4c899684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            md5.update(block)
    return md5.hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the md5 hash of a file.

    >>> get_file_hash_from_file('test.txt', block_size=2 ** 20)
    'e3b0c44298fc1c149afbf4c899684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            md5 = hashlib.md5()
            while True:
                data = f.read(block)
                if not data:
                    break
                md5.update(data)
            md5 = md5.hexdigest()
            if md5 == md5:
               