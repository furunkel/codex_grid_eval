def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text:
        raise ValueError("text cannot be empty")
    if not isinstance(text, bytes):
        raise TypeError("text must be a bytes")
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    If 'filename' is a directory, return its contents as a string.
    Otherwise, return None.
    """
    if not os.path.exists(filename):
        return None
    if not os.path.isdir(filename):
        return None
    return open(filename).read()


def get_file_contents_as_string(filename):
    """
    Given a filename, return its contents as a string.
    If 'filename' is a directory, return its contents as a string.
    Otherwise, return None.
    """
    if not os.path.exists(filename):
        return None
    return open(filename).read()


def get_file_contents_as_lines(filename):
    """
    Given a filename, return its contents as a list of lines.
    If 'filename' is a directory, return its contents as a list of lines.
    Otherwise, return None.
    """
    if not os.path.exists(filename):
        return None
    return open(filename).readlines()


def get_file_contents_as_string_with_newlines(filename):
    """
    Given a filename, return its contents as a string with newlines.
    If 'filename' is a directory, return its contents as a string with newlines.
    Otherwise, return None.
    """
    if not os.path.exists(filename):
        return None
    return open(filename).read().replace("\n", os.linesep)


def get_file_contents_as_lines_with_newlines(filename):
    """
    Given a filename, return its contents as a list of lines with newlines.
    If 'filename' is a directory, return its contents as a list of lines with newlines.
    Otherwise, return