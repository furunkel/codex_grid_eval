
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest eleventh value.
    """
    return max(lst[11])

# Test your function
some_func([(7, 8, 9), (4, 5, 6), (10, 11, 12)])
</cell>
<text>
Problem 3
Use a list comprehension to create a list of the first letters of every word in the string below:

"The quick brown fox jumps over the lazy dog"


becomes

['T', 'h', 'e', 'r', 'q', 'b', 'r', 'w', 'o', 'v', 's', 'f', 'x', 'j', 'm', 'p', 'l', 'o', 'z', 'g', 'd']


Hint: You may want to use split() here and be careful with punctuation.


</text>
<cell>
# Write your function below:
def first_letters(s):
    """
    Given a string s, return a list containing the first letters of each word in the string.
    
    >>> first_letters("The quick brown fox jumps over the lazy dog")
    ['T', 'h', 'e', 'r', 'q', 'b', 'r', 'w', 'o', 'v', 's', 'f', 'x', 'j', 'm', 'p', 'l', 'o', 'z', 'g', 'd']
    """
    
    # Initialize an empty list
    lst = []
    
    # Split the string into a list of words
    words = s.split()
    
    # Iterate through the list of words
    for word in words:
        
        # Append the first letter of each word to the empty list
        lst.append(word[0])
    
    # Return the list
    return lst

# Test your function
first_letters("The quick brown fox jumps over the lazy dog")
</cell>
<text>
Problem 4
Create a set of all the colors of rainbow and set it to the variable colors_rainbow.


</text>
<cell>
# Write your set solution below:
colors_rainbow = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
</cell>
<text>
Problem 5
Create a set of the colors that are in both colors_rainbow and colors_not_rainbow. Add this set to the variable colors_in_both.


</text>
<cell>
# Write your set solution below:
colors_in_both = colors_rainbow.intersection(colors_not_rainbow)
</cell>
<text>
Problem 6
Create a list containing all the even indexed letters in the string below:

"The quick brown fox jumps over the lazy dog"


becomes

['T', 'h', 'i', 's', 'q', 'b', 'r', 'w', 'o', 'v', 's', 'f', 'x', 'j', 'm', 'p', 'l', 'o', 'z', 'g', 'd']


Hint: You may want to use split() here and be careful with punctuation.


</text>
<cell>