def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    if isinstance(text, str):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    elif isinstance(text, unicode):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    else:
        raise TypeError('Expected string or unicode, got %r' % type(text))


def get_file_hash(filename):
    """
    Given a filename, return its hash.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    """
    with open(filename, 'rb') as f:
        return f.read()


def get_file_lines(filename):
    """
    Given a filename, return its lines as a list of strings.
    """
    with open(filename, 'rb') as f:
        return f.readlines()


def get_line_count(filename, lineno):
    """
    Given a filename, return its line count.
    """
    with open(filename, 'rb') as f:
        return len(f.readlines())


def get_line_count_for_file(filename, lineno):
    """
    Given a filename, return its line count for the given file.
    """
    with open(filename, 'rb') as f:
        return len(f.readlines())


def get_line_count_for_file_and_line(filename, lineno):
    """
    Given a filename, return its line count for the given file and line.
    """
    with open(filename, 'rb') as f:
        return len(f.readlines())


def get_line_count_for_file_and_full_path(filename, lineno):
    """
    Given a filename, return its line count for the given file and full path.
    """
    with open(filename, 'rb') as f:
        return len(f.readlines())


def get_line_count_for_file_and_full_path_and