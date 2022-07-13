
def string_to_hash(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if text == '':
        return None
    h = sha384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_of_file(path):
    """
    Given a path to a file, return its sha384 hash equivalent string.
    If 'path' is an empty string, return None.

    >>> hash_of_file('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if path == '':
        return None
    h = sha384()
    with open(path, 'rb') as fd:
        while True:
            chunk = fd.read(4096)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def hash_of_string(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if text == '':
        return None
    h = sha384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_of_file(path):
    """
    Given a path to a file, return its sha384 hash equivalent string.
    If 'path' is an empty string, return None.

    >>> hash_of_file('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if path == '':
        return None
    h = sha384()
    with open(path, 'rb') as fd:
        while True:
            chunk = fd.read(4096)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def hash_of_string(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if text == '':
        return None
    h = sha