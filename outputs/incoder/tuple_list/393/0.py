
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x:x[2])[-1]
</cell>
<cell>
some_func([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Problem 3
Write a function that takes a string and returns the number of words in the string.


</text>
<cell>
def count_words(text):
    """
    Given a string, return the number of words in the string.
    """
    
    # Your code here
    
    return len(text.split())
</cell>
<cell>
count_words('The quick brown fox jumps over the lazy dog')
</cell>
<text>
Problem 4
Write a function that takes a string and returns the number of characters in the string.


</text>
<cell>
def count_characters(text):
    """
    Given a string, return the number of characters in the string.
    """
    
    # Your code here
    
    return len(text)
</cell>
<cell>
count_characters('The quick brown fox jumps over the lazy dog')
</cell>
<text>
Problem 5
Write a function that takes a string and returns the number of uppercase and lowercase letters in the string.


</text>
<cell>
def count_uppercase_lowercase(text):
    """
    Given a string, return the number of uppercase and lowercase letters in the string.
    """
    
    # Your code here
    
    return sum(c.isupper() for c in text) + sum(c.islower() for c in text)
</cell>
<cell>
count_uppercase_lowercase('The quick brown fox jumps over the lazy dog')
</cell>
<text>
Problem 6
Write a function that takes a string and returns the number of characters in the string that are not uppercase or lowercase letters.


</text>
<cell>
def count_non_letters(text):
    """
    Given a string, return the number of characters in the string that are not uppercase or lowercase letters.
    """
    
    # Your code here
    
    return sum(c.isalpha() for c in text)
</cell>
<cell>
count_non_letters('The quick brown fox jumps over the lazy dog')
</cell>
<text>
Problem 7
Write a function that takes a string and returns the number of characters in the string that are not digits.


</text>
<cell>
def count_non_digits(text):
    """
    Given a string, return the number of characters in the string that are not digits.
    """
    
    # Your code here
    
    return sum(c.isdigit() for c in text)
</cell>
<cell>
count_non_digits('The quick brown 