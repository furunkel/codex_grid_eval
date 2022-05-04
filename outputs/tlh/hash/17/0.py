
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH md-5 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('md5') == '1bc29b36f623ba82aaf6724fd3b16718'
    """
    return hashlib.md5(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha1 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_qIj('sha1') == '86f7e437faa5a7fce15d1ddcb9eaeaea377667b8'
    """
    return hashlib.sha1(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_chorgh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_chorgh('sha256') == '603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4'
    """
    return hashlib.sha256(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_ghom(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghom('sha512') == 'bfd76c0ebbd006fee583410547c1887b0292be76d582d96c242d2a792723e3fd895f6dd898e295e7a1e0e729db3d7bceb6c2c2d22488b2b7fb814dca552ef