
def string_to_hash(text):
    """
    Given a string 'text', return its SHA384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    else:
        return hashlib.sha384(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a SHA384 hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b') == '0'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha384(hash.encode('utf-8')).hexdigest()


def hash_to_int(hash):
    """
    Given a SHA384 hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b') == 0
    """
    if hash == '':
        return None
    else:
        return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its SHA384 hash equivalent.
    If 'integer' is 0, return None.

    >>> int_to_hash(0) == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if integer == 0:
        return None
    else:
        return hashlib.sha384(str(integer).encode('utf-8')).hexdigest()


def hash_to_base64(hash):
    """
    Given a SHA384 hash 'hash', return its base