
def solve(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains one or more question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "?4321"
    solve("ab") = "aB"
    solve("#a@C") = "#a@c"
    """
    if '?' in s:
        return s[::-1]
    else:
        return ''.join([i.swapcase() if i.isalpha() else i for i in s])

def solve(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains one or more question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "?4321"
    solve("ab") = "aB"
    solve("#a@C") = "#a@c"
    """
    if '?' in s:
        return s[::-1]
    else:
        return ''.join([i.swapcase() if i.isalpha() else i for i in s])

def solve(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains one or more question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "?4321"
    solve("ab") = "aB"
    solve("#a@C") = "#a@c"
    """
    if '?' in s:
        return s[::-1]
    else:
        return ''.join([i.swapcase() if i.isalpha() else i for i in s])

def solve(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains one or more question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") =