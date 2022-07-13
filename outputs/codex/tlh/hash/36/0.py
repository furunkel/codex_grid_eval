
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha224(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_sha256(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha256(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_sha384(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha384 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha384(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_sha512(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha512(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_sha3_224(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3_224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha3_224(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_sha3_256(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3_256 hash ghopDu.
    qaSbe'chugh, v