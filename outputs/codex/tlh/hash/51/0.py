
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    return hashlib.sha224(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    return hashlib.sha224(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_ghItlh('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    return hashlib.sha224(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_ghItlh_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_ghItlh_ghItlh('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845