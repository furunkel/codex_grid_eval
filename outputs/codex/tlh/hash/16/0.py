
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH md-5 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('sha1') == '74a89174426b40307102e165374ab8ab'
    """
    return hashlib.md5(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(filename):
    """
    Ach batlh ghIlghameS 'filename' neH md-5 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('test/test_data/test_file.txt') == 'd41d8cd98f00b204e9800998ecf8427e'
    """
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def ghop_D_hash_file_sha1(filename):
    """
    Ach batlh ghIlghameS 'filename' neH sha1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_sha1('test/test_data/test_file.txt') == 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def ghop_D_hash_file_sha256(filename):
    """
    Ach batlh ghIlghameS 'filename' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_sha256('test/test_data/test_file.txt') == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

