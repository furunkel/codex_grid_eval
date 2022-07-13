
def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    return re.sub(r'\d+', lambda match: match.group() * 2, string) \
           .replace('A', 'aa').replace('B', 'bb').replace('C', 'cc') \
           .replace('D', 'dd').replace('E', 'ee').replace('F', 'ff') \
           .replace('G', 'gg').replace('H', 'hh').replace('I', 'ii') \
           .replace('J', 'jj').replace('K', 'kk').replace('L', 'll') \
           .replace('M', 'mm').replace('N', 'nn').replace('O', 'oo') \
           .replace('P', 'pp').replace('Q', 'qq').replace('R', 'rr') \
           .replace('S', 'ss').replace('T', 'tt').replace('U', 'uu') \
           .replace('V', 'vv').replace('W', 'ww').replace('X', 'xx') \
           .replace('Y', 'yy').replace('Z', 'zz')

# ______________________________________________________________________________
# Strings

def fix_quotes(string):
    """
    Given a string, return a version where any single-quote characters have been replaced with two
    single-quote characters.
    """
    mapping = {'"': '''"''',
               '‘': '''‘''',
               '’': '''’''',
               '‚': '''‚''',
               '“': '''“''',
               '”': '''”''',
               '„': '''„''',
               '†': '''†''',
               '‡': '''‡''',
               '⁂': '''⁂''',
               '⁃': '''⁃''',
               '⁄': '''⁄''',
               '⁅': '''⁅''',
               '⁆': '''⁆''',
               '⁇': '''⁇''',
               '⁈': '''⁈''',
               '⁉': '''⁉''',
               '⁊': '''⁊''',
               '⁋': '''⁋''',
               '⁌': '''⁌''',
               '⁍': '''⁍''',
               '⁎': '''⁎''',
               '⁏': '''⁏''',
               '⁐': '''⁐''',
               '⁑': '''⁑''',
               '⁒': '''⁒''',
               '⁓': '''⁓''',
               '⁔': '''⁔''',
               '⁕': '''⁕''