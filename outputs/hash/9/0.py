
def string_to_hash(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('cfcd208495d565ef66e7dff9f98764da') == '0'
    """
    if hash == '':
        return None
    else:
        return hash_to_string_dict[hash]


def hash_to_string_dict_init():
    """
    Initialize the hash_to_string_dict dictionary.
    """
    global hash_to_string_dict
    hash_to_string_dict = {}
    for i in range(len(string_to_hash_dict)):
        hash_to_string_dict[string_to_hash_dict[i]] = i


def string_to_hash_dict_init():
    """
    Initialize the string_to_hash_dict dictionary.
    """
    global string_to_hash_dict
    string_to_hash_dict = {}
    for i in range(len(hash_to_string_dict)):
        string_to_hash_dict[i] = hash_to_string_dict[i]


def hash_to_string_dict_save(filename):
    """
    Save the hash_to_string_dict dictionary to a file.
    """
    with open(filename, 'wb') as f:
        pickle.dump(hash_to_string_dict, f)


def hash_to_string_dict_load(filename):
    """
    Load the hash_to_string_dict dictionary from a file.
    """
    global hash_to_string_dict
    with open(filename, 'rb') as f:
        hash_to_string_dict = pickle.load(f)


def string_to_hash_dict_save(filename):
    """
    Save the string_to_hash_dict dictionary to a file.
    """
