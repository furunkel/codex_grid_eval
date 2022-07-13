
def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text).hexdigest()


def get_hash_of_file(file_path):
    """
    Given a file path, return its md-5 hash equivalent string.
    If the file does not exist, return None.

    >>> get_hash_of_file('test_files/test_file_1.txt') == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if not os.path.isfile(file_path):
        return None
    else:
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()


def get_hash_of_dir(dir_path):
    """
    Given a directory path, return its md-5 hash equivalent string.
    If the directory does not exist, return None.

    >>> get_hash_of_dir('test_files/test_dir_1') == 'd41d8cd98f00b204e9800998ecf8427e'
    """
    if not os.path.isdir(dir_path):
        return None
    else:
        hash_list = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                hash_list.append(get_hash_of_file(os.path.join(root, file)))
        return hashlib.md5(''.join(hash_list)).hexdigest()


def get_hash_of_dir_recursive(dir_path):
    """
    Given a directory path, return its md-5 hash equivalent string.
    If the directory does not exist, return None.

    >>> get_hash_of_dir_recursive('test_files/test_dir_1') == 'd41d8cd98f00b204e9800998ecf8427e'
    """
    if not os.path.isdir(dir_path):
        return None
    else:
        hash_list = []
        for root, dirs, files in os.walk