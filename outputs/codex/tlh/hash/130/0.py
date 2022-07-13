
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    return blake2s(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    return blake2s(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_ghItlh('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    return blake2s(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_ghItlh_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_ghItlh_ghItlh('sha1') == 'cd9b4f43951c6e4547d4701e