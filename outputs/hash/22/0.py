
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if text == '':
        return None
    else:
        return blake2s(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a BLAKE2S hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f') == 'Hello world'
    """
    if hash == '':
        return None
    else:
        return blake2s(bytes.fromhex(hash)).decode('utf-8')


def hash_to_int(hash):
    """
    Given a BLAKE2S hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f') == 160874909898410090790872408749098984100907908724087490989841009079087240874909898410090790872408749098984100907908724087490989841009079087240874909898410090790872408749098984100907908724087490989841009079087240874909898410090790872408749098984100907908724087490989841009079087240874909898410090790872408749098984100907908724087490989841009079087240874909898410090790872408749098984100907908