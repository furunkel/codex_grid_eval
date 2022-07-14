def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Return the SHA256 hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def get_file_path(filename):
    """
    Return the absolute path to the file.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))


def get_file_name(filename):
    """
    Return the filename without the extension.
    """
    return os.path.splitext(filename)[0]


def get_file_path_and_name(filename):
    """
    Return the absolute path and name of the file.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))


def get_file_name_and_path(filename):
    """
    Return the absolute path and name of the file.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))


def get_file_path_and_name_and_extension(filename):
    """
    Return the absolute path and name of the file.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))


def get_file_name_and_extension_and_path(filename):
    """
    Return the absolute path and name of the file.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))


def get_file_path_and_name_and_extension_and_path(filename):
    """
    Return the absolute path and name of the file.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))


def get_file_name_and_extension_and_path_and_name(filename):
    """
    Return