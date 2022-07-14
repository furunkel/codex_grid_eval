def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if not text:
        return None
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Return the sha-224 hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha224(f.read()).hexdigest()


def get_file_contents(filename):
    """
    Return the contents of the file.
    """
    with open(filename, 'rb') as f:
        return f.read()


def get_file_lines(filename):
    """
    Return the lines of the file.
    """
    with open(filename, 'rb') as f:
        return f.readlines()


def get_file_hash_lines(filename):
    """
    Return the lines of the file, as a list of strings.
    """
    with open(filename, 'rb') as f:
        return [line.strip() for line in f.readlines()]


def get_file_hash_lines(filename):
    """
    Return the lines of the file, as a list of strings.
    """
    with open(filename, 'rb') as f:
        return [line.strip() for line in f.readlines()]


def get_file_lines_with_hashes(filename):
    """
    Return the lines of the file, as a list of strings.
    """
    with open(filename, 'rb') as f:
        return [line.strip() for line in f.readlines() if line.startswith('SHA-224')]


def get_file_lines_with_hashes_and_lines(filename):
    """
    Return the lines of the file, as a list of strings.
    """
    with open(filename, 'rb') as f:
        return [line.strip() for line in f.readlines() if line.startswith('SHA-224')]


def get_file_hash_lines_with_