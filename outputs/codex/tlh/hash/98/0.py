
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hallo welt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    return hashlib.sha512(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA512 hash ghopDu' qIj.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_qIj('Hallo welt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    return ghop_D_hash(vIdaj).upper()

def ghop_D_hash_qIj_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA512 hash ghopDu' qIj.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_qIj_qIj('Hallo welt') == '9C12B8EB6BC215A7D2202EAA0F255D5DBD6F6D820BBD7D936D7771691ACB952904EF6A679FF4BF9063F44CC4F219504312EA313E63C7CF60E01EDD1F570A3EDB'
    """
    return ghop_D_hash(vIdaj).upper()

def ghop_D_hash_qIj_qIj_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA512 hash ghopDu' qIj.
    qaSbe'chugh, vaj 'vIdaj