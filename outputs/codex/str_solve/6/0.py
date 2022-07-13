
def solve(s):
    """You are given a string s.
    if s[i] is a vowel, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("1234?") = "?4321"
    solve("ab") = "Ab"
    solve("#a@C") = "#A@C"
    """
    if not s:
        return s
    vowels = "aeiou"
    result = ""
    for c in s:
        if c.isalpha():
            if c.lower() in vowels:
                result += c.swapcase()
            else:
                result += c
        else:
            result += c
    return result[::-1]

def solve(s):
    """You are given a string s.
    if s[i] is a vowel, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("1234?") = "?4321"
    solve("ab") = "Ab"
    solve("#a@C") = "#A@C"
    """
    if not s:
        return s
    vowels = "aeiou"
    result = ""
    for c in s:
        if c.isalpha():
            if c.lower() in vowels:
                result += c.swapcase()
            else:
                result += c
        else:
            result += c
    return result[::-1]

def solve(s):
    """You are given a string s.
    if s[i] is a vowel, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("1234?") = "?4321"
    solve("ab") = "Ab"
    solve("#a@C") = "#A@C"
    """
    if not s:
        return s
    vowels = "aeiou"
    result = ""
    for c in s:
        if c.isalpha():
            if c.lower() in vowels:
                result += c.swapcase()
            else:
                result += c
        else:
           