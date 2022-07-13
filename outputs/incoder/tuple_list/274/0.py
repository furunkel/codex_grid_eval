
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest eleventh value.
    """
    
    lst = sorted(lst)
    
    return lst[-11][1]
</cell>
<cell>
fibonacci([(3,2), (1,1), (5,1), (7,1), (9,1), (11,1), (13,1), (17,1), (19,1), (23,1), (29,1), (31,1), (37,1), (43,1), (49,1), (55,1), (61,1), (67,1), (73,1), (79,1), (83,1), (89,1), (97,1)])
</cell>
<text>
Problem 7
Write a function that takes a string and returns the number of words in the string.


</text>
<cell>
def count_words(text):
    """
    Given a string, return the number of words in the string.
    """
    
    return len(text.split())
</cell>
<cell>
count_words('The quick brown fox jumps over the lazy dog')
</cell>
<text>
Problem 8
Write a function that takes a string and returns the number of characters in the string.


</text>
<cell>
def count_characters(text):
    """
    Given a string, return the number of characters in the string.
    """
    
    return len(text)
</cell>
<cell>
count_characters('The quick brown fox jumps over the lazy dog')
</cell>
<text>
Problem 9
Write a function that takes a string and returns the number of uppercase characters in the string.


</text>
<cell>
def count_uppercase_characters(text):
    """
    Given a string, return the number of uppercase characters in the string.
    """
    
    return len([c for c in text if c.isupper()])
</cell>
<cell>
count_uppercase_characters('The quick brown fox jumps over the lazy dog')
</cell>
<text>
Problem 10
Write a function that takes a string and returns the number of lowercase characters in the string.


</text>
<cell>
def count_lowercase_characters(text):
    """
    Given a string, return the number of lowercase characters in the string.
    """
    
    return len([c for c in text if c.islower()])
</cell>
<cell>
count_lowercase_characters('The quick brown fox jumps over the lazy dog')
</cell>
<text>
Problem 11
Write a function that takes a string and returns the number of characters in the string that start with a capital letter.


</text>
<cell>
def count_capital_characters(text):
    """
    Given a string, return the number of characters in the string that start with a capital letter.
    """
    
    return len([