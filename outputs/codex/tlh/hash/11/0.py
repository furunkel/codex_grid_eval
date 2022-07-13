
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH MD5 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('md5') == '1bc29b36f623ba82aaf6724fd3b16718'
    """
    return hashlib.md5(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(filename):
    """
    Ach batlh ghIlghameS 'filename' neH MD5 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('test.txt') == '1bc29b36f623ba82aaf6724fd3b16718'
    """
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def ghop_D_hash_file_sha1(filename):
    """
    Ach batlh ghIlghameS 'filename' neH SHA1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_sha1('test.txt') == 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def ghop_D_hash_file_sha256(filename):
    """
    Ach batlh ghIlghameS 'filename' neH SHA256 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_sha256('test.txt') == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def ghop_D_hash_file_sha512(filename):
    """
    Ach batlh ghIlgh