def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('sha1') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.sha1(filename).hexdigest()


def get_file_hash_from_file(filename):
    """
    Given a filename, return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash_from_file('sha1') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib