
def string_to_hash(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b'
    """
    if text == '':
        return None
    return hashlib.sha3_512(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b') == 'Hallo welt'
    """
    if hash == '':
        return None
    return hashlib.sha3_512(bytes.fromhex(hash)).hexdigest()


def hash_to_string_with_salt(hash, salt):
    """
    Given a hash 'hash' and a salt 'salt', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string_with_salt('4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b', 'salt') == 'Hallo welt'
    """
    if hash == '':
        return None
    return hashlib.sha3_512((bytes.fromhex(hash) + salt.encode('utf-8'))).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a salt 'salt', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('Hallo welt', 'salt') == '4bc49cca273fb299acf8f8991b6547b6232a2344f289ed