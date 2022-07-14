def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    return None


def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    """
    with open(filename, 'r') as f:
        return f.read()


def get_file_lines(filename):
    """
    Given a filename, return its contents as a list of lines.
    """
    with open(filename, 'r') as f:
        return f.readlines()


def get_line_count(filename, lineno):
    """
    Given a filename, return its line count.
    """
    with open(filename, 'r') as f:
        return len(f.readlines())


def get_line_count_for_file(filename, lineno):
    """
    Given a filename, return its line count for the given file.
    """
    with open(filename, 'r') as f:
        return len(f.readlines())


def get_line_count_for_file_and_line(filename, lineno):
    """
    Given a filename, return its line count for the given file and line.
    """
    with open(filename, 'r') as f:
        return len(f.readlines())


def get_line_count_for_file_and_line_no_return(filename, lineno):
    """
    Given a filename, return its line count for the given file and line.
    """
    with open(filename, 'r') as f:
        return len(f.readlines())


def get_line_count_for_file_and_line_with_return(filename, lineno):
    """
    Given a filename, return its line count for the given file and line.
    """
    with open(filename, 'r') as f:
        return len(f.readlines())


def get_line_count_for_file_and_line_no_return_and_line(filename, lineno):
    """
    Given a filename, return its line count for the given file and line.