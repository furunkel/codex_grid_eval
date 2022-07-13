
def string_to_hash(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b'
    """
    if text == '':
        return None
    return sha3_512(text.encode('utf-8')).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('Hallo welt') == '4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b'
    """
    if text == '':
        return None
    return sha3_512(text.encode('utf-8')).hexdigest()


def string_to_hash_hex_array(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_array('Hallo welt') == ['4bc49cca', '273fb299', 'acf8f899', '1b6547b6', '232a234f', '289ed60db', '3159ac50', '01df5c24', 'bc157546', '565e701a', '514608ee', 'ecde9c9b', 'ac18619b', '39132b96', 'ddf28d2b', 'c2c25b']
    """
    if text == '':
        return None
    return sha3_512(text.encode('utf-8')).hexdigest()


def string_to_hash_hex_array(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_array('Hallo welt') == ['4bc49cca', '273fb299', 'acf8f899', '1b6547b6', '232a234f', '289ed60db', '3159ac50', '01df5c24', 'bc157546', '565e701a', '514608ee', 'ecde9c9b', 'ac18619b', '39132b96', 'ddf28d2b', 'c2c25b']
    """
    if text == '':
        return None
    return sha3_512(text.encode('utf-8')).hexdigest()


def string_to_hash_hex_array(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_array('Hallo welt') == ['4bc49cca', '273fb299