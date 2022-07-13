
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA384 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    return hashlib.sha384(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA384 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    return hashlib.sha384(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA384 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_ghItlh('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    return hashlib.sha384(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_ghItlh_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA384 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_ghItlh_ghItlh('