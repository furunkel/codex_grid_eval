
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA384 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('md5') == '86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d'
    """
    return hashlib.sha384(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_vaj_ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA384 hash ghopDu' vaj
    'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_vaj_ghop_D_hash('md5') == '86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d'
    """
    return ghop_D_hash(ghop_D(vIdaj))

def ghop_D_hash_vaj_ghop_D_hash_vaj_ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA384 hash ghopDu' vaj
    'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_vaj_ghop_D_hash_vaj_ghop_D_hash('md5') == '86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d'
    """
    return ghop_D_hash(ghop_D_hash(ghop_D(vIdaj)))

def ghop_D_hash_vaj_ghop_D_hash_vaj_ghop_D_hash_vaj_ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA384 hash ghopDu' vaj
    'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D