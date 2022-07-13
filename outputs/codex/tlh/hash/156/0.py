
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3-512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha3_512(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_vaj_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3-512 hash ghopDu' vaj
    ghopDu'vam 'vIdaj' po'vaD qaS wanI'vam.
    """
    return ghop_D_hash(ghop_D_vaj_ghItlh(vIdaj))

def ghop_D_vaj_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3-512 hash ghopDu' vaj
    ghopDu'vam 'vIdaj' po'vaD qaS wanI'vam.
    """
    return vIdaj.encode('utf-8')

def ghop_D_vaj_ghItlh_vaj_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3-512 hash ghopDu' vaj
    ghopDu'vam 'vIdaj' po'vaD qaS wanI'vam.
    """
    return ghop_D_vaj_ghItlh(ghop_D_vaj_ghItlh(vIdaj))

def ghop_D_vaj_ghItlh_vaj_ghItlh_vaj_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3-512 hash ghopDu' vaj
    ghopDu'vam 'vIdaj' po'vaD qaS wanI'vam.
    """
    return ghop_D_vaj_ghItlh(ghop_D_vaj_ghItlh(ghop_D_vaj_ghItlh(vIdaj)))

def ghop_D