
def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1'
    """
    if text == '':
        return None
    return blake2b_hash(text)


def blake2b_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_hash('sha1') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1'
    """
    return blake2b(text, digest_size=32)


def blake2b_hash_hexdigest(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_hash_hexdigest('sha1') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1'
    """
    return blake2b(text, digest_size=32).hexdigest()


def blake2b_hash_hexdigest_bytes(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_hash_hexdigest_bytes('sha1') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1'
    """
    return blake2b(text, digest_size=32).hexdigest().encode()


def blake2b_hash_hexdigest_bytes_len(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_hash_hexdigest_bytes_len('sha1') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b75