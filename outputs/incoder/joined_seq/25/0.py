
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with a dash and False otherwise.
    """
    
    # your code here
    
    return bool(re.search(r'[a-z]+-[a-z]+', text))
</cell>
<cell>
# run this cell to test your function
joined_sequence("Hello World!")
</cell>
<text>
Question 3
Write a function that returns a list of all the words in the text that only contain letters a-z and A-Z.

Hint: You may want to use Python's filter function.


</text>
<cell>
# UNQ_C3 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# UNIT TEST COMMENT: Candidate for Table Driven Tests
# GRADED FUNCTION: get_words
def get_words(text):
    '''
    Input:
        text: a string
    Output:
        a list of all the words in the text that only contain letters a-z and A-Z
    '''
    
    # your code here
    
    return list(filter(lambda x: re.search(r'[a-z]+', x), text.split()))
</cell>
<cell>
# run this cell to test your function
get_words("The quick brown fox jumps over the lazy dog")
</cell>
<text>
Question 4
Write a function that returns a list of all the words in the text that have length greater than or equal to 3.

Sample Test Cases:

Input: "The quick brown fox jumps over the lazy dog"

Output: ["brown", "fox", "dog"]

</text>
<cell>
# UNQ_C4 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# UNIT TEST COMMENT: Candidate for Table Driven Tests
# GRADED FUNCTION: get_words
def get_words(text):
    '''
    Input:
        text: a string
    Output:
        a list of all the words in the text that have length greater than or equal to 3
    '''
    
    # your code here
    
    return list(filter(lambda x: len(x) >= 3, text.split()))
</cell>
<cell>
# run this cell to test your function
get_words("The quick brown fox jumps over the lazy dog")
</cell>
<text>
Question 5
Write a function that returns a list of all the words in the text that have length less than 3.

Sample Test Cases:

Input: "The quick brown fox jumps over the lazy dog"

Output: []

</text>
<cell>
# UNQ_C5 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# UNIT TEST COMMENT: Candidate for Table Driven Tests
# GRADED FUNCTION: get_words
def get_words(text):
