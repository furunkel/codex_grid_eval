
def string_to_hash(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return sha384(text).hexdigest()


def hash_to_string(hash):
    """
    Given a sha384 hash string, return its string equivalent.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    return sha384(hash).hexdigest()


def hash_of_file(filename):
    """
    Given a filename, return the sha384 hash of its contents.
    If 'filename' is an empty string, return None.
    """
    if filename == '':
        return None
    with open(filename, 'rb') as f:
        return sha384(f.read()).hexdigest()


def hash_of_string(string):
    """
    Given a string 'string', return its sha384 hash equivalent string.
    If 'string' is an empty string, return None.
    """
    if string == '':
        return None
    return sha384(string).hexdigest()


def hash_of_file(filename, blocksize=65536):
    """
    Given a filename and a blocksize, return the sha384 hash of its contents.
    If 'filename' is an empty string, return None.
    """
    if filename == '':
        return None
    with open(filename, 'rb') as f:
        return sha384(f.read(blocksize)).hexdigest()


def hash_of_string(string, blocksize=65536):
    """
    Given a string 'string' and a blocksize, return the sha384 hash of its contents.
    If 'string' is an empty string, return None.
    """
    if string == '':
        return None
    return sha384(string, blocksize).hexdigest()


def hash_of_file(filename, blocksize=65536):
    """
    Given a filename and a blocksize, return the sha384 hash of its contents.
    If 'filename' is an empty string, return None.
    """
    if filename == '':
        return None
    with open(filename, 'rb') as f:
        return sha384(f.read(blocksize)).hexdigest()


def hash_of_string(string, blocksize=65536):
    """
    Given a string 'string' and a blocksize, return the sha384 hash of its contents.
    If 'string' is an empty string, return None.
    """
    if string == '':
        return None
    return sha384(string, blocksize).hexdigest()


def hash_of_file(filename, blocksize=65536):
    """
    Given a filename and a blocksize, return the sha384 hash of its contents.
    If 'filename' is an empty string, return None.
    """
    if filename == '':
        return None
    with open(filename, 'rb') as f:
        return sha384(f.read(blocksize)).hexdigest()


def hash_of_string(string, blocksize=65536):
    """
    Given a string 'string' and a blocksize, return the sha384 hash of its contents.
    If 'string' is an 