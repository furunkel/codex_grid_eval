
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der BLAKE2B-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    if text == '':
        return None
    else:
        return blake2b(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein BLAKE2B-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87') == 'md5'
    """
    if hash == '':
        return None
    else:
        return blake2b(hash.encode('utf-8'), digest_size=len(hash)).hexdigest()


def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll der BLAKE2B-Hash dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_mit_salt('md5', 'salt') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
   