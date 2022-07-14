def string_to_hash(text):
    """
    Given a string 'text', return its SHA384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if not text:
        return None
    if len(text) == 40:
        return hashlib.sha384(text).hexdigest()
    else:
        return None


def get_file_hash(filename):
    """
    Given a filename, return its SHA384 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if not filename:
        return None
    if len(filename) == 40:
        return hashlib.sha384(filename).hexdigest()
    else:
        return None


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if not filename:
        return None
    if len(filename) == 40:
        return os.path.getsize(filename)
    else:
        return None


def get_file_md5(filename):
    """
    Given a filename, return its MD5 equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f