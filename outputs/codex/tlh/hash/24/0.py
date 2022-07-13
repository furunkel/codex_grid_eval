
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA1 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha1(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_vaj_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA1 hash ghopDu' vaj
    ghaH 'vIdaj' po'vaD qaS wanI'vam.
    """
    return ghop_D_hash(vIdaj) + ' ' + vIdaj

def ghop_D_hash_vaj_ghItlh_vaj_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA1 hash ghopDu' vaj
    ghaH 'vIdaj' po'vaD qaS wanI'vam.
    """
    return ghop_D_hash(vIdaj) + ' ' + vIdaj + ' ' + vIdaj

def ghop_D_hash_vaj_ghItlh_vaj_ghItlh_vaj_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA1 hash ghopDu' vaj
    ghaH 'vIdaj' po'vaD qaS wanI'vam.
    """
    return ghop_D_hash(vIdaj) + ' ' + vIdaj + ' ' + vIdaj + ' ' + vIdaj

def ghop_D_hash_vaj_ghItlh_vaj_ghItlh_vaj_ghItlh_vaj_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA1 hash ghopDu' vaj
    ghaH 'vIdaj' po'vaD qaS wanI'vam.
    """
    return ghop_D_hash(vIdaj) + ' ' + vIdaj + ' ' + vIdaj + ' ' + vIdaj + ' ' +