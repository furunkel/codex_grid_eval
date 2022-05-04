
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return blake2s(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is None, return an empty string.
    """
    if hash is None:
        return ''
    else:
        return hash.decode('utf-8')


def get_hash_value(hash):
    """
    Given a hash 'hash', return its integer value.
    If 'hash' is None, return 0.
    """
    if hash is None:
        return 0
    else:
        return int(hash, 16)


def get_hash_range(hash):
    """
    Given a hash 'hash', return its range.
    If 'hash' is None, return 0.
    """
    if hash is None:
        return 0
    else:
        return int(hash, 16) % 256


def get_hash_range_list(hash):
    """
    Given a hash 'hash', return a list of its range.
    If 'hash' is None, return [0].
    """
    if hash is None:
        return [0]
    else:
        return [int(hash, 16) % 256]


def get_hash_range_list_from_string(text):
    """
    Given a string 'text', return a list of its range.
    If 'text' is an empty string, return [0].
    """
    if text == '':
        return [0]
    else:
        return [int(blake2s(text.encode('utf-8')).hexdigest(), 16) % 256]


def get_hash_range_list_from_string_list(text_list):
    """
    Given a list of strings 'text_list', return a list of its range.
    If 'text_list' is an empty list, return [0].
    """
    if len(text_list) == 0:
        return [0]
    else:
        return [int(blake2