
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1'
    """
    if text == '':
        return None
    return blake2b(text.encode(), digest_size=DIGEST_SIZE)


def hash_to_string(hash):
    """
    Given a BLAKE2B hash string, return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1') == 'sha1'
    """
    if hash is None:
        return None
    return blake2s(hash, digest_size=DIGEST_SIZE).decode()


def hash_exists(hash):
    """
    Given a BLAKE2B hash string, return whether it exists.
    If 'hash' is an empty string, return False.

    >>> hash_exists('ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1')
    True
    """
    if hash is None:
        return False
    return bool(blake2b(hash.encode(), digest_size=DIGEST_SIZE))


def hash_exists(hash):
    """
    Given a BLAKE2B hash string, return whether it exists.
    If 'hash' is an empty string, return False.

    >>> hash_exists('ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1')
    True
    """
    if hash is None:
        return False
    return bool(blake2b(hash.encode(), digest_size=DIGEST_SIZE))


def hash_exists(hash):
    """
    Given a BLAKE2B hash string, return whether it exists.
    If 'hash' is an empty string, return False.

    >>> hash_exists('ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9