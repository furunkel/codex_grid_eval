
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains more than one question mark, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "1234?"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    if s.count('?') > 1:
        return s[::-1]
    else:
        return ''.join([i.lower() if i.isupper() else i.upper() for i in s])

def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains more than one question mark, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "1234?"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    if s.count('?') > 1:
        return s[::-1]
    else:
        return ''.join([i.lower() if i.isupper() else i.upper() for i in s])

def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains more than one question mark, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "1234?"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    if s.count('?') > 1:
        return s[::-1]
    else:
        return ''.join([i.lower() if i.isupper() else i.upper() for i in s])

def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains more than one question mark, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
