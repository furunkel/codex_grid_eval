
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-256 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha256(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_sha1(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-1 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha1(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_md5(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH md5 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.md5(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_sha512(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha512(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_sha384(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-384 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return hashlib.sha384(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_sha224(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po