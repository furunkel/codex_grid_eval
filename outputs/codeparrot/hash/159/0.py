def string_to_hash(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '2d44da53f305ab94b6365837b9803627ab098c41a6013694f9b468bccb9c13e95b3900365eb58924de7158a54467e984efcfdabdbcc9af9a940d49c51455b04c'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha3(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha3-512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('0') == '2d44da53f305ab94b6365837b9803627ab098c41a6013694f9b468bccb9c13e95b3900365eb58924de7158a54467e984efcfdabdbcc9af9a940d49c51455b04c'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.sha3(filename).hexdigest()


def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    If 'filename' is an empty string, return None.

    >>> get_file_contents('0') == '2d44da53f305ab94b6365837b9803627ab098c41a6013694f9b468bccb9c13e95b3900365eb58924de7158a54467e984efcfdabdbcc9af9a940d49c51455b04c'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return open(filename).read()


def get_file_contents_as_string(filename):
    """
    Given a filename, return its contents as