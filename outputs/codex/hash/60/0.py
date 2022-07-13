
def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def get_hash_of_file(file_path):
    """
    Given a file path 'file_path', return its SHA256 hash equivalent string.
    If 'file_path' is an empty string, return None.
    """
    if file_path == '':
        return None
    else:
        with open(file_path, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()


def get_hash_of_dir(dir_path):
    """
    Given a directory path 'dir_path', return its SHA256 hash equivalent string.
    If 'dir_path' is an empty string, return None.
    """
    if dir_path == '':
        return None
    else:
        return hashlib.sha256(dir_path.encode('utf-8')).hexdigest()


def get_hash_of_dir_recursive(dir_path):
    """
    Given a directory path 'dir_path', return its SHA256 hash equivalent string.
    If 'dir_path' is an empty string, return None.
    """
    if dir_path == '':
        return None
    else:
        return hashlib.sha256(dir_path.encode('utf-8')).hexdigest()


def get_hash_of_dir_recursive_with_file_contents(dir_path):
    """
    Given a directory path 'dir_path', return its SHA256 hash equivalent string.
    If 'dir_path' is an empty string, return None.
    """
    if dir_path == '':
        return None
    else:
        return hashlib.sha256(dir_path.encode('utf-8')).hexdigest()


def get_hash_of_dir_recursive_with_file_paths(dir_path):
    """
    Given a directory path 'dir_path', return its SHA256 hash equivalent string.
    If 'dir_path' is an empty string, return