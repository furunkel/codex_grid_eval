
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


def blake2b_salted_hash(text, salt):
    """
    Given a string 'text' and a 'salt', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_salted_hash('sha1', 'salt') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1'
    """
    return blake2b(text + salt, digest_size=32)


def blake2b_salted_hash_with_prefix(text, salt, prefix):
    """
    Given a string 'text' and a 'salt' and a prefix 'prefix', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_salted_hash_with_prefix('sha1', 'salt', 'prefix') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1'
    """
    return blake2b(prefix + text + salt, digest_size=32)


def blake2b_salted_hash_with_prefix_and_salt(text, salt, prefix, salt):
    """
    Given a string 'text' and a 'salt' and a prefix 'prefix' and a 'salt', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_salted_hash_