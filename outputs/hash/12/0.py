
def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def get_hash_of_file(file_path):
    """
    Given a file path, return its md-5 hash equivalent string.
    If the file does not exist, return None.
    """
    if not os.path.exists(file_path):
        return None
    else:
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()


def get_hash_of_directory(directory_path):
    """
    Given a directory path, return its md-5 hash equivalent string.
    If the directory does not exist, return None.
    """
    if not os.path.exists(directory_path):
        return None
    else:
        hash_list = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                hash_list.append(get_hash_of_file(file_path))
        return hashlib.md5(str(hash_list).encode('utf-8')).hexdigest()


def get_hash_of_directory_tree(directory_path):
    """
    Given a directory path, return its md-5 hash equivalent string.
    If the directory does not exist, return None.
    """
    if not os.path.exists(directory_path):
        return None
    else:
        hash_list = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                hash_list.append(get_hash_of_file(file_path))
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                hash_list.append(get_hash_of_directory(dir_path))
        return hashlib.md5(str(hash_list).en