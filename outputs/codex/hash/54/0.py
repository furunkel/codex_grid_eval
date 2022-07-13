
def string_to_hash(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_to_string(hash_value):
    """
    Given a hash value 'hash_value', return its string equivalent.
    If 'hash_value' is an empty string, return None.
    """
    if hash_value == '':
        return None
    else:
        return hash_value.encode('utf-8')


def get_hash_value(text):
    """
    Given a string 'text', return its hash value.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return string_to_hash(text)


def get_string(hash_value):
    """
    Given a hash value 'hash_value', return its string equivalent.
    If 'hash_value' is an empty string, return None.
    """
    if hash_value == '':
        return None
    else:
        return hash_to_string(hash_value)


def get_block_value(block_string):
    """
    Given a block string, return its block value.
    If 'block_string' is an empty string, return None.
    """
    if block_string == '':
        return None
    else:
        return json.loads(block_string)


def get_block_string(block_value):
    """
    Given a block value, return its block string.
    If 'block_value' is an empty string, return None.
    """
    if block_value == '':
        return None
    else:
        return json.dumps(block_value, sort_keys=True)


def get_block_hash(block_value):
    """
    Given a block value, return its block hash.
    If 'block_value' is an empty string, return None.
    """
    if block_value == '':
        return None
    else:
        return string_to_hash(get_block_string(block_value))


def