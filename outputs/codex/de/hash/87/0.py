
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha-384-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    else:
        return hashlib.sha384(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein sha-384-Hash 'hash' (als Zeichenkette). Zurückgegen werden soll
    die zugehörige Zeichenkette.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b') == '0'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha384(bytes.fromhex(hash)).hexdigest()


def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll der sha-384-Hash von 'text' mit 'salt' als Salt (wiederum als
    Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_mit_salt('0', '0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    else:
        return hashlib.sha384(text.encode('utf-8') + salt.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette_