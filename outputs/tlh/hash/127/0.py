
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    return blake2s(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu' qIj.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_qIj('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    return blake2s(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_qIj_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu' qIj.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_qIj_qIj('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    return blake2s(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_qIj_qIj_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu' qIj.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_qIj_qIj_qIj('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf