
def solve(s):
    """You are given a string s.
    if s[i] is a vowel, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("1234?") = "1234?"
    solve("ab") = "bA"
    solve("#a@C") = "C@A#"
    """
    if '?' not in s:
        return s[::-1]
    else:
        vowels = 'aeiouAEIOU'
        new_s = ''
        for i in s:
            if i in vowels:
                if i.isupper():
                    new_s += i.lower()
                else:
                    new_s += i.upper()
            else:
                new_s += i
        return new_s

print(solve("1234"))
print(solve("1234?"))
print(solve("ab"))
print(solve("#a@C"))