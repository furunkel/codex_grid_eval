
def solve(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("1234?") = "?4321"
    solve("ab") = "aB"
    solve("#a@C") = "#a@c"
    """
    if not s:
        return s
    vowels = "aeiou"
    result = ""
    for c in s:
        if c.isalpha():
            if c.lower() in vowels:
                result += c
            else:
                result += c.swapcase()
        else:
            result += c
    return result


def solve(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("1234?") = "?4321"
    solve("ab") = "aB"
    solve("#a@C") = "#a@c"
    """
    if not s:
        return s
    vowels = "aeiou"
    result = ""
    for c in s:
        if c.isalpha():
            if c.lower() in vowels:
                result += c
            else:
                result += c.swapcase()
        else:
            result += c
    return result


def solve(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("1234?") = "?4321"
    solve("ab") = "aB"
    solve("#a@C") = "#a@c"
    """
    if not s:
        return s
    vowels = "aeiou"
    result = ""
    for c in s:
        if c.isalpha():
            if c.lower() in vowels:
                result += c
            else:
                result += c.swapcase()
        else:
            result += c
    return