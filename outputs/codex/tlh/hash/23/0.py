
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha1 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    return hashlib.sha1(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(file_path):
    """
    Ach batlh ghIlghameS 'file_path' neH sha1 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file(__file__) == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    with open(file_path, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def ghop_D_hash_file_md5(file_path):
    """
    Ach batlh ghIlghameS 'file_path' neH md5 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_md5(__file__) == 'c1ea94f7e524679d0cf34ab7b0b28abe'
    """
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def ghop_D_hash_file_sha256(file_path):
    """
    Ach batlh ghIlghameS 'file_path' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_sha256(__file__) == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def ghop_D_hash_file_sha