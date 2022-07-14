def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    return None


def get_file_hash(filename):
    """
    Given a filename, return its hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return hashlib.sha1(filename.encode('utf-8')).hexdigest()
    return None


def get_file_path(filename):
    """
    Given a filename, return its path equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return filename
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


def get_file_name(filename):
    """
    Given a filename, return its name equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return filename
    return os.path.basename(filename)


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return os.path.getsize(filename)
    return None


def get_file_date(filename):
    """
    Given a filename, return its date equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return filename
    return os.path.getctime(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename))


def get_file_size_in_milliseconds(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
       