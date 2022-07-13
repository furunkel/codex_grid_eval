
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA512-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein SHA512-Hash 'hash'. Zurückgegen werden soll die zugehörige
    Zeichenkette.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548') == 'md5'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha512(hash.encode('utf-8')).hexdigest()


def zeichenkette_zu_hash_und_zurueck(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll die zugehörige
    Zeichenkette.
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_und_zurueck('md5') == 'md5'
    """
    if text == '':
        return None
    else:
        return hash_zu_zeichenkette(zeichenkette_zu_hash(text))


def zeichenkette_zu_hash_und_zurueck_2(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll die zugehörige
    Zeichenkette.
    Ist 'text' eine leere Zeichenkette, soll None zurü