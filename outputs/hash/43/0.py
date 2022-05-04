
def string_to_hash(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    else:
        return hashlib.sha224(text.encode('utf-8')).hexdigest()


def string_to_hash_file(text, filename):
    """
    Given a string 'text', write its SHA224 hash equivalent string to a file 'filename'.
    If 'text' is an empty string, write None to 'filename'.

    >>> string_to_hash_file('Hello world', 'hash.txt')
    >>> open('hash.txt').read() == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        with open(filename, 'w') as f:
            f.write(str(None))
    else:
        with open(filename, 'w') as f:
            f.write(hashlib.sha224(text.encode('utf-8')).hexdigest())


def string_from_hash_file(filename):
    """
    Given a file 'filename', return its SHA224 hash equivalent string.
    If 'filename' is an empty file, return None.

    >>> string_from_hash_file('hash.txt') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    with open(filename, 'r') as f:
        if f.read() == '':
            return None
        else:
            return hashlib.sha224(f.read().encode('utf-8')).hexdigest()


def string_to_hash_file_bin(text, filename):
    """
    Given a string 'text', write its SHA224 hash equivalent string to a file 'filename' in binary mode.
    If 'text' is an empty string, write None to 'filename'.

    >>> string_to_hash_file_bin('Hello world', 'hash.bin')
    >>> open('hash.bin', 'rb').read() == b'\xac#\x0f\x15\xfc\xae\x7