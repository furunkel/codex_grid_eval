
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-1 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    return hashlib.sha1(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(filename):
    """
    Ach batlh ghIlghameS 'filename' neH sha-1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('test/test_data/test_file.txt') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def ghop_D_hash_file_md5(filename):
    """
    Ach batlh ghIlghameS 'filename' neH md5 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_md5('test/test_data/test_file.txt') == 'c1ea94f7e524679d0cf34ab7b0b28abe'
    """
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def ghop_D_hash_file_sha256(filename):
    """
    Ach batlh ghIlghameS 'filename' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_sha256('test/test_data/test_file.txt') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def ghop_D_hash_file_