def string_to_hash(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '2d44da53f305ab94b6365837b9803627ab098c41a6013694f9b468bccb9c13e95b3900365eb58924de7158a54467e984efcfdabdbcc9af9a940d49c51455b04c'
    """
    if not text:
        return None
    text = text.strip()
    if len(text) == 0:
        return None
    return hashlib.sha3_512(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its SHA3_512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('0') == '2d44da53f305ab94b6365837b9803627ab098c41a6013694f9b468bccb9c13e95b3900365eb58924de7158a54467e984efcfdabdbcc9af9a940d49c51455b04c'
    """
    if not filename:
        return None
    filename = filename.strip()
    if len(filename) == 0:
        return None
    return hashlib.sha3_512(filename).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('0') == '2d44da53f305ab94b6365837b9803627ab098c41a6013694f9b468bccb9c13e95b3900365eb58924de7158a54467e984efcfdabdbcc9af9a940d49c51455b04c'
    """
    if not filename:
        return None
    filename = filename.strip()
    if len(filename) == 0:
        return None
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its