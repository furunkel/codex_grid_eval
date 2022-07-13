
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
    vowels = ["a", "e", "i", "o", "u"]
    vowels_lower = ["a", "e", "i", "o", "u"]
    vowels_upper = ["A", "E", "I", "O", "U"]
    vowels_lower = [x.lower() for x in vowels_lower]
    vowels_upper = [x.upper() for x in vowels_upper]
    vowels_lower = [x for x in vowels_lower if x not in vowels]
    vowels_upper = [x for x in vowels_upper if x not in vowels]
    vowels_lower = [x for x in vowels_lower if x not in vowels_upper]
    vowels_upper = [x for x in vowels_upper if x not in vowels_lower]
    vowels_lower = [x for x in vowels_lower if x not in vowels_upper]
    vowels_upper = [x for x in vowels_upper if x not in vowels_lower]
    vowels_lower = [x for x in vowels_lower if x not in vowels_upper]
    vowels_upper = [x for x in vowels_upper if x not in vowels_lower]
    vowels_lower = [x for x in vowels_lower if x not in vowels_upper]
    vowels_upper = [x for x in vowels_upper if x not in vowels_lower]
    vowels_lower = [x for x in vowels_lower if x not in vowels_upper]
    vowels_upper = [x for x in vowels_upper if x not in vowels_lower]
    vowels_lower = [x for x in vowels_lower if x not in vowels_upper]
    vowels_upper = [x for x in vowels_upper if x not in vowels_lower]
    vowels_lower = [x for x in vowels_lower if x not in vowels_upper]
    vowels_upper = [x for x in vowels_upper if x not in vowels_lower]
    vowels_lower = [x for x in vowels_lower if x not in vowels_upper]
    vowels_upper = [x for x in vowels_upper if x not in vowels_lower]
    vowels_lower = [x for x in vowels_lower if x not in vowels_upper]
    vowels_upper = [x for x in vowels_upper if x not in vowels_lower]
    vowels_lower = [x for x in vowels_lower if x not in vowels_upper]
    vowels_upper = [x for x in vowels_upper if x not in vowels_lower]
    vowels_lower = [x for x in vowels_lower if x not in vowels_upper]
    vowels_upper = [x for x in vowels_upper if x not in vowels_lower]
    vowels_lower = [x for x in vowels_lower if x not in vowels_upper]
    vowels_upper = [x for x in 