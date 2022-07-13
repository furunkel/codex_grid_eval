def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 1 bit position.
    """
    return int(a[0] - b[0]) != int(a[1] - b[1])


def get_all_files(path):
    """
    Returns all files in a directory.
    """
    return [os.path.join(path, f) for f in os.listdir(path)]


def get_all_dirs(path):
    """
    Returns all directories in a directory.
    """
    return [os.path.join(path, d) for d in os.listdir(path)]


def get_all_files_in_dir(path):
    """
    Returns all files in a directory.
    """
    return [os.path.join(path, f) for f in os.listdir(path)]


def get_all_dirs_in_dir(path):
    """
    Returns all directories in a directory.
    """
    return [os.path.join(path, d) for d in os.listdir(path)]


def get_all_files_in_dir_in_dir(path):
    """
    Returns all files in a directory.
    """
    return [os.path.join(path, f) for f in os.listdir(path)]


def get_all_dirs_in_dir_in_dir(path):
    """
    Returns all directories in a directory.
    """
    return [os.path.join(path, d) for d in os.listdir(path)]


def get_all_files_in_dir_in_dir_in_dir(path):
    """
    Returns all files in a directory.
    """
    return [os.path.join(path, f) for f in os.listdir(path)]


def get_all_dirs_in_dir_in_dir_in_dir(path):
    """
    Returns all directories in a directory.
    """
    return [os.path.join(path, d) for d in os.listdir(path)]


def get_all_files_in_dir_in_dir_in_dir(path):
    """
    Returns all files in a directory.
    """
    return [os.path.join(path, f) for f in os.