
def string_to_hash(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.
    """

def get_file_hash(filename):
    """
    Given a filename, return its sha3-512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    else:
        return hashlib.sha3_512(open(filename, 'rb').read()).hexdigest()

def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    else:
        return open(filename, 'rb').read()

def get_file_lines(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    else:
        return open(filename, 'rb').readlines()

def get_file_lines_with_hashes(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    else:
        return open(filename, 'rb').readlines()

def get_file_lines_with_hashes_and_lines(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    else:
        return open(filename, 'rb').readlines()

def get_file_lines_with_hashes_and_lines_and_hashes(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    else:
        return open(filename, 'rb').readlines()

def get_file_lines_with_hashes_and_lines_and_hashes_and_lines(filename):
    """
    Given a filename, return its lines as a list of strings.
    If '