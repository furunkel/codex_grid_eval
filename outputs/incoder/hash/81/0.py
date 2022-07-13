
def string_to_hash(text):
    """
    Given a string 'text', return its SHA384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    return sha384(text).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its SHA384 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    return sha384(text).hexdigest()


def string_to_hash_hex_lowercase(text):
    """
    Given a string 'text', return its SHA384 hash equivalent hex string in lowercase.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_lowercase('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    return sha384(text).hexdigest().lower()


def string_to_hash_hex_uppercase(text):
    """
    Given a string 'text', return its SHA384 hash equivalent hex string in uppercase.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_uppercase('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    return sha384(text).hexdigest().upper()


def string_to_hash_hex_casefold(text):
    """
    Given a string 'text', return its SHA384 hash equivalent hex string in lowercase.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_casefold('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    return sha384(text).hexdigest().casefold()


def string_to_hash_hex_casefold_lowercase(text):
    """
    Given a string 'text', return its SHA384 hash equivalent hex string in 