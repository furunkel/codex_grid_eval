
def string_to_hash(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
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


def hash_matches(text, hash):
    """
    Given a string 'text' and a hash 'hash', return True if the hash of 'text'
    matches 'hash'. Return False otherwise.

    >>> hash_matches('Hello world', 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c')
    True
    >>> hash_matches('Hello world', 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0d')
    False
    """
    return string_to_hash(text) == hash


def get_hash_value(hash):
    """
    Given a hash 'hash', return its integer value.
    If 'hash' is an empty string, return None.

    >>> get_hash_value('e2e1