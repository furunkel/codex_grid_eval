
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

    >>> hash_to_int('619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f') == 160872409898410090798818119396196434121984700041491917295508859975173310
    """
    if hash == '':
        return None
    else:
        return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its BLAKE2S hash equivalent string.
    If 'integer' is 0, return None.

    >>> int_to_hash(160872409898410090798818119396196434121984700041491917295508859975173310) == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if integer == 0:
        return None
    else:
        return hex(integer)[2:]


def hash_to_bytes(hash):
    """
    Given