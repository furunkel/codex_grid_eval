
def solve(s):
    """You are given a string s.
    if s[i] is a vowel, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains exactly one question mark, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "?4321"
    solve("ab") = "Ab"
    solve("#a@C") = "#A@C"
    """
    if s.count('?') == 1:
        return s[::-1]
    else:
        return ''.join([i.upper() if i.lower() in 'aeiou' else i.lower() for i in s])

def solve(s):
    """You are given a string s.
    if s[i] is a vowel, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains exactly one question mark, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "?4321"
    solve("ab") = "Ab"
    solve("#a@C") = "#A@C"
    """
    if s.count('?') == 1:
        return s[::-1]
    else:
        return ''.join([i.upper() if i.lower() in 'aeiou' else i.lower() for i in s])

def solve(s):
    """You are given a string s.
    if s[i] is a vowel, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains exactly one question mark, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "?4321"
    solve("ab") = "Ab"
    solve("#a@C") = "#A@C"
    """
    if s.count('?') == 1:
        return s[::-1]
    else:
        return ''.join([i.upper() if i.lower() in 'aeiou' else i.lower() for i in s])

def solve(s):
    """You are given a string s.
    if s[i] is a vowel, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains exactly one question mark, reverse the string.
    The function should return the resulted string.
   