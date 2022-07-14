def string_to_hash(text):
    """
    Given a string 'text', return its SHA384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if not text:
        return None
    return hashlib.sha384(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its SHA384 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('hello.txt') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if not filename:
        return None
    return hashlib.sha384(filename.encode('utf-8')).hexdigest()


def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    If 'filename' is an empty string, return None.

    >>> get_file_contents('hello.txt') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if not filename:
        return None
    with open(filename, 'r') as f:
        return f.read()


def get_file_lines(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.

    >>> get_file_lines('hello.txt') == ['9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1