
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "house" if n >= 2000 (and neither if -100 <= n < 2000).
    """
    if n < -100:
        return "mouse"
    elif n >= 2000:
        return "house"
    else:
        return "none"

# Write a function that takes a string and returns the number of words in the string.
def count_words(s):
    """
        Given a string s, return the number of words in s.
    """
    return len(s.split())

# Write a function that takes a string and returns the number of characters in the string.
def count_characters(s):
    """
        Given a string s, return the number of characters in s.
    """
    return len(s)

# Write a function that takes a string and returns the number of lines in the string.
def count_lines(s):
    """
        Given a string s, return the number of lines in s.
    """
    return s.count("\n")

# Write a function that takes a string and returns the number of characters in the string without spaces.
def count_characters_no_spaces(s):
    """
        Given a string s, return the number of characters in s without spaces.
    """
    return len(s.replace(",", ""))

# Write a function that takes a string and returns the number of words in the string without spaces.
def count_words_no_spaces(s):
    """
        Given a string s, return the number of words in s without spaces.
    """
    return len(s.replace(",", "").split())

# Write a function that takes a string and returns the number of characters in the string without spaces.
def count_characters_no_spaces_no_commas(s):
    """
        Given a string s, return the number of characters in s without spaces.
    """
    return len(s.replace(",", "").replace(":", ""))

# Write a function that takes a string and returns the number of words in the string without spaces.
def count_words_no_spaces_no_commas(s):
    """
        Given a string s, return the number of words in s without spaces.
    """
    return len(s.replace(",", "").replace(":", "").split())

# Write a function that takes a string and returns the number of characters in the string without spaces.
def count_characters_no_spaces_no_commas_no_colons(s):
    """
        Given a string s, return the number of characters in s without spaces.
    """
    return len(s.replace(",", "").replace(":", "").replace(";", ""))

# Write a function that takes a string and returns the number of words in the string without spaces.
def count_words_no_spaces_no_commas_no_colons(s):
    """
        Given a string s, return the number of words in s without spaces.
    """
    return len(s.replace(",", "").replace(":", "").replace(";", "").split())

# Write a function that takes a string and returns the number of characters in the string without spaces.
def count_characters_no_spaces_no_commas_no_colons_no_periods(s):
    """
        Given a string s, return the number of characters in s without 