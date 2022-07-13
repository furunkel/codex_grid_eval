
def solve(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "1234?"
    solve("ab") = "Ba"
    solve("#a@C") = "c@a#"
    """
    if s.isalpha():
        return s[::-1]
    else:
        return ''.join([i.swapcase() if i.isalpha() else i for i in s])

def solve(s):
    return s[::-1].swapcase() if s.isalpha() else ''.join([i.swapcase() if i.isalpha() else i for i in s])

def solve(s):
    return s[::-1].swapcase() if s.isalpha() else ''.join(i.swapcase() if i.isalpha() else i for i in s)

def solve(s):
    return s[::-1].swapcase() if s.isalpha() else ''.join(i.swapcase() if i.isalpha() else i for i in s)

def solve(s):
    return s[::-1].swapcase() if s.isalpha() else ''.join(i.swapcase() if i.isalpha() else i for i in s)

def solve(s):
    return s[::-1].swapcase() if s.isalpha() else ''.join(i.swapcase() if i.isalpha() else i for i in s)

def solve(s):
    return s[::-1].swapcase() if s.isalpha() else ''.join(i.swapcase() if i.isalpha() else i for i in s)

def solve(s):
    return s[::-1].swapcase() if s.isalpha() else ''.join(i.swapcase() if i.isalpha() else i for i in s)

def solve(s):
    return s[::-1].swapcase() if s.isalpha() else ''.join(i.swapcase() if i.isalpha() else i for i in s)

def solve(s):
    return s[::-1].swapcase() if s.isalpha() else ''.join(i.swapcase() if i.isalpha() else i for i in s)

def solve(s):
    return s[::-1