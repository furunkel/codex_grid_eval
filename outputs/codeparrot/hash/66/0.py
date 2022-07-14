def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.sha256(text.encode('utf-8')).hexdigest()
    return None


def get_file_content(path, encoding='utf-8'):
    """
    Given a path, return the content of 'path' as a string.
    """
    with open(path, 'rb') as f:
        return f.read().decode(encoding)


def get_file_lines(path, encoding='utf-8'):
    """
    Given a path, return the lines of 'path' as a list of strings.
    """
    with open(path, 'rb') as f:
        return f.readlines()


def get_file_lines_with_encoding(path, encoding='utf-8'):
    """
    Given a path, return the lines of 'path' as a list of strings.
    """
    with open(path, 'rb') as f:
        return f.readlines(encoding)


def get_file_lines_with_encoding_and_errors(path, encoding='utf-8'):
    """
    Given a path, return the lines of 'path' as a list of strings.
    """
    with open(path, 'rb') as f:
        return f.readlines(encoding, errors='replace')


def get_file_lines_with_encoding_and_errors_and_newlines(path, encoding='utf-8'):
    """
    Given a path, return the lines of 'path' as a list of strings.
    """
    with open(path, 'rb') as f:
        return f.readlines(encoding, errors='replace').splitlines()


def get_file_lines_with_encoding_and_errors_and_newlines_and_newlines(path, encoding='utf-8'):
    """
    Given a path, return the lines of 'path' as a list of strings.
    """
    with open(path, 'rb') as f:
        return f.readlines(encoding, errors='replace').splitlines(True)


def get_file_lines_with_encoding_and_errors_and_newlines_and_newlines