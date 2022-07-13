
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    return hashlib.sha512(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA512 hash ghopDu' qIj.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_qIj('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    return ghop_D_hash(ghop_D_hash(vIdaj))

def ghop_D_hash_qIj_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA512 hash ghopDu' qIj qIj.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_qIj_qIj('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    return ghop_D_hash(ghop_D_hash_qIj(vIdaj))

def ghop_D_hash_qIj_qIj_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA512 hash ghopDu' qIj q