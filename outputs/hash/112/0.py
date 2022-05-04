
def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1'
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=32).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1') == 'sha1'
    """
    if hash == '':
        return None
    return blake2b(bytes.fromhex(hash), digest_size=32).hexdigest()


def string_to_hash_to_string(text):
    """
    Given a string 'text', return its string equivalent.
    If 'text' is an empty string, return None.

    >>> string_to_hash_to_string('sha1') == 'sha1'
    """
    if text == '':
        return None
    return blake2b(blake2b(text.encode('utf-8'), digest_size=32).digest(), digest_size=32).hexdigest()


def hash_to_string_to_hash(hash):
    """
    Given a hash 'hash', return its hash equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string_to_hash('ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda