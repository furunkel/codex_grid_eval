
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA256 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha256(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_vaj_ghItlh(vIdaj, ghItlh):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA256 hash ghopDu' 'ghItlh'
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha256((vIdaj + ghItlh).encode('utf-8')).hexdigest()

def ghop_D_hash_vaj_ghItlh_vaj_ghItlh(vIdaj, ghItlh1, ghItlh2):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA256 hash ghopDu' 'ghItlh1' 'ghItlh2'
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha256((vIdaj + ghItlh1 + ghItlh2).encode('utf-8')).hexdigest()

def ghop_D_hash_vaj_ghItlh_vaj_ghItlh_vaj_ghItlh(vIdaj, ghItlh1, ghItlh2, ghItlh3):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA256 hash ghopDu' 'ghItlh1' 'ghItlh2' 'ghItlh3'
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha256((vIdaj + ghItlh1 + ghItlh2 + ghItlh3).encode('utf-8')).hexdigest()

def ghop_D_hash_vaj_ghItlh_vaj_ghItlh