
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("1234?") = "1234?"
    solve("ab") = "BA"
    solve("#a@C") = "c@A#"
    """
    if '?' not in s:
        return s[::-1]
    else:
        return ''.join([i.swapcase() if i.isalpha() else i for i in s])

# Test Cases

print(solve("1234"))
print(solve("1234?"))
print(solve("ab"))
print(solve("#a@C"))