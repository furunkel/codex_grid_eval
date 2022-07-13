
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if text == '':
        return None
    else:
        return blake2s(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a BLAKE2S hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c') == 'Hallo welt'
    """
    if hash == '':
        return None
    else:
        return blake2s(bytes.fromhex(hash)).decode('utf-8')


def hash_to_hash(hash):
    """
    Given a BLAKE2S hash 'hash', return its BLAKE2S hash equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_hash('0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if hash == '':
        return None
    else:
        return blake2s(bytes.fromhex(hash)).hexdigest()


def hash_to_int(hash):
    """
    Given a BLAKE2S hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c') == 5242880
    """
    if hash == '':
        return None
    else:
        return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its BLAKE2S hash equivalent