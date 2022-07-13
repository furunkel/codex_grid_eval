
def string_to_hash(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '2d44da53f305ab94b6365837b9803627ab098c41a6013694f9b468bccb9c13e95b3900365eb58924de7158a54467e984efcfdabdbcc9af9a940d49c51455b04c'
    """
    if text == '':
        return None
    h = hashlib.sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_address(text, network='mainnet'):
    """
    Given a string 'text', return its address equivalent in 'network'.
    If 'text' is an empty string, return None.

    >>> string_to_address('0', network='mainnet') == '0x0000000000000000000000000000000000000000'
    True
    >>> string_to_address('0x0000000000000000000000000000000000000000', network='mainnet') == '0'
    True
    >>> string_to_address('0', network='testnet') == '0x0000000000'
    True
    >>> string_to_address('0x0000000000', network='testnet') == '0'
    True
    >>> string_to_address('0', network='livenet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='livenet') == '0'
    True
    >>> string_to_address('0x00000000', network='testnet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='livenet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='testnet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='livenet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='testnet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='livenet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='testnet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='livenet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='testnet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='livenet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='testnet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='livenet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='testnet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='livenet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='testnet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='livenet') == '0x00000000'
    True
    >>> string_to_address('0x00000000', network='testnet') == '0x00000000'
    True
    >>> string_to_address('0x00000000