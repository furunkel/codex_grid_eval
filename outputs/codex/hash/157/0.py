
def string_to_hash(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c'
    """
    if text == '':
        return None
    return hashlib.sha3_512(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c') == 'Hello world'
    """
    if hash == '':
        return None
    return hashlib.sha3_512(bytes.fromhex(hash)).hexdigest()


def string_to_hash_to_string(text):
    """
    Given a string 'text', return its string equivalent.
    If 'text' is an empty string, return None.

    >>> string_to_hash_to_string('Hello world') == 'Hello world'
    """
    if text == '':
        return None
    return hash_to_string(string_to_hash(text))


def hash_to_string_to_hash(hash):
    """
    Given a hash 'hash', return its hash equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string_to_hash('e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c') == 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d