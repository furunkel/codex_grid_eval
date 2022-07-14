def string_to_hash(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c'
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

    >>> get_file_hash('Hello world') == 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c'
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

    >>> get_file_contents('Hello world') == 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return open(filename).read()


