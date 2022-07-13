
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    return blake2s(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_vaj_ghop_D(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_vaj_ghop_D('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    return blake2s(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_vaj_ghop_D_vaj_ghop_D(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_vaj_ghop_D_vaj_ghop_D('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    return blake2s(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_vaj_ghop_D_vaj_ghop_D_vaj_ghop_D(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_vaj_ghop_D_vaj_