
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA3_512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hello world') == 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c'
    """
    return hashlib.sha3_512(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA3_512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh('Hello world') == 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c'
    """
    return hashlib.sha3_512(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_ghItlh_chIS(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA3_512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_chIS('Hello world') == 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c'
    """
    return hashlib.sha3_512(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_ghItlh_chIS_chIS(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA3_512 hash ghopDu.
    qaSbe