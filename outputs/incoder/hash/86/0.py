
def string_to_hash(text):
    """
    Given a string 'text', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_to_string(hash):
    """
    Given a sha-384 hash string 'hash', return its string representation.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049') == 'Hallo welt'
    """
    if hash == '':
        return None
    return binascii.hexlify(hash).decode('utf-8')


def hash_to_int(hash):
    """
    Given a sha-384 hash string 'hash', return its integer representation.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049') == 4258273254
    """
    if hash == '':
        return None
    return int(binascii.hexlify(hash).decode('utf-8'), 16)


def int_to_hash(n):
    """
    Given an integer 'n', return its sha-384 hash equivalent string.
    If 'n' is an empty string, return None.

    >>> int_to_hash(4258273254) == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    if n == 0:
        return None
    h = hashlib.sha3_384()
    h.update(str(n).encode('utf-8'))
    return h.hexdigest()


def int_to_string(i, length=32):
    """
    Given an integer 'i', return a string 'i' of length 'length'.
    If 'i' is an empty string, return None.

    >>> int_to_string(4258273254) == '4258273254'
    """
    if i == '':
        return None
    return str(i)[:length]


def int_to_hash_str(i):
    """
    Given an integer 'i', return a string 'i' of length 'length'.
    If 'i' is an empty string, return None.

    >>> int_to_hash_str(4258273254