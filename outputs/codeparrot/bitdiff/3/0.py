def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 1 bit position.
    """
    return int(a[0] != b[0]) - int(a[1] != b[1])


def get_all_files(directory):
    """
    Returns a list of all files in a directory.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)]


def get_all_files_in_directory(directory):
    """
    Returns a list of all files in a directory.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)]


def get_all_files_in_directory_with_extension(directory, extension):
    """
    Returns a list of all files in a directory with the given extension.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if f.endswith(extension)]


def get_all_files_in_directory_with_extension_in_directory(directory, extension):
    """
    Returns a list of all files in a directory with the given extension in the given directory.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if f.endswith(extension) and os.path.isfile(os.path.join(directory, f))]


def get_all_files_in_directory_with_extension_in_directory_with_extension_in_directory(directory, extension):
    """
    Returns a list of all files in a directory with the given extension in the given directory.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if f.endswith(extension) and os.path.isfile(os.path.join(directory, f))]


def get_all_files_in_directory_with_extension_in_directory_with_extension_in_directory_with_extension_in_directory(directory, extension):
    """
    Returns a list of all files in a directory with the given extension in the given directory.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if f.endswith(extension