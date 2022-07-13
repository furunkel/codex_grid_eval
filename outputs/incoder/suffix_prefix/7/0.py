
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('prefix')
    ['p', 'pr', 'pre', 'pref', 'prefi', 'prefix']
    """
    return list(itertools.takewhile(lambda s: len(s) <= len(string), itertools.accumulate(string.split(), lambda s, x: s + x)))


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('suffix')
    ['s', 'su', 'suf', 'suffix', 'sufix', 'sufixi', 'sufixia', 'sufixias', 'sufixiae', 'sufixiasu', 'sufixiase', 'sufixiases', 'sufixiasue', 'sufixiasux', 'sufixiasuxs', 'sufixiasuxse', 'sufixiasuxses', 'sufixiasuxsez', 'sufixiasuxsezh', 'sufixiasuxsezhj', 'sufixiasuxsezhjl', 'sufixiasuxsezhjlk', 'sufixiasuxsezhjlka', 'sufixiasuxsezhjlkaa', 'sufixiasuxsezhjlkaaa', 'sufixiasuxsezhjlkaaaa', 'sufixiasuxsezhjlkaaaab', 'sufixiasuxsezhjlkaaaac', 'sufixiasuxsezhjlkaaaaca', 'sufixiasuxsezhjlkaaaacaa', 'sufixiasuxsezhjlkaaaacaaa', 'sufixiasuxsezhjlkaaaacaaaa', 'sufixiasuxsezhjlkaaaacaaaab', 'sufixiasuxsezhjlkaaaacaaaac', 'sufixiasuxsezhjlkaaaacaaaaca', 'sufixiasuxsezhjlkaaaacaaaacaa', 'sufixiasuxsezhjlkaaaacaaaacaaa', 'sufixiasuxsezhjlkaaaacaaaacaaaa', 'sufixiasuxsezhjlkaaaacaaaacaaaab', 'sufixiasuxsezhjlkaaaacaaaacaaaac', 'sufixiasuxsezhjlkaaaacaaaacaaaaca', 'sufixiasuxsezhjl