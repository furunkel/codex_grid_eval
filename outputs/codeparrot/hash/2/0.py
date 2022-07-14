def string_to_hash(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '05b7f4cbafdb32436fe8928f41ed8f64'
    """
    if not text:
        return None
    text = text.strip()
    if text.startswith('md5='):
        return text[6:]
    return None


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the md5 hash for a file.

    >>> get_file_hash('somefile.txt')
    '0d5e6b7a831c399e269772661e2e4f9e'
    """
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the md5 hash for a file.

    >>> get_file_hash_from_file('somefile.txt')
    '0d5e6b7a831c399e269772661e2e4f9e'
    """
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def get_file_hash_from_url(url, block_size=2 ** 20):
    """
    Calculate the md5 hash for a file.

    >>> get_file_hash_from_url('http://www.google.com/images/srpr/logo3w.png')
    '0d5e6b7a831c399e269772661e2e4f9e'
    """
    md5 = hashlib.md5()
    with open(url, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)
    return md