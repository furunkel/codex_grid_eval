
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2b hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    return blake2b(vIdaj.encode('utf-8'), digest_size=64).hexdigest()


def ghop_D_hash_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2b hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    return blake2b(vIdaj.encode('utf-8'), digest_size=64).hexdigest()


def ghop_D_hash_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2b hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_ghItlh('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    return blake2b(vIdaj.encode('utf-8'), digest_size=64).hexdigest()


def ghop_D_hash_ghItlh_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh gh