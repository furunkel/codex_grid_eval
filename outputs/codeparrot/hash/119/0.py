def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    return None


def get_file_hash(filename):
    """
    Given a filename, return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return hashlib.sha1(filename.encode('utf-8')).hexdigest()
    return None


def get_file_hash_from_file(filename):
    """
    Given a filename, return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash_from_file('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return hashlib.sha1(filename.