
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of uppercase letters joined with an underscore and False otherwise.
    """
    
    sequence = False
    
    for letter in text:
        if letter.isupper() and letter != ' ':
            sequence = True
            
        if sequence:
            if letter.isupper():
                sequence = False
            else:
                sequence = True
                
    return sequence
</cell>
<cell>
# Test your code
joined_sequence("Hello World")
</cell>
<text>
Expected output: True

</text>
<cell>
# Put your code here
joined_sequence("Hello World!")
</cell>
<text>
Expected output: False

</text>
<text>
Write a function that takes as input a string and returns the number of uppercase letters present in the string.

For example if the input string is "Hello World" the output should be 4.

If the input string has less than 4 letters return 0.

This is case sensitive, for example "a" is considered different from "A".


</text>
<cell>
def count_uppercase_letters(text):
    """
    Write a function that takes as input a string and returns the number of uppercase letters present in the string.
    """
    
    count = 0
    
    for letter in text:
        if letter.isupper():
            count += 1
            
    return count
</cell>
<cell>
# Test your code
count_uppercase_letters("Hello World")
</cell>
<text>
Expected output: 4

</text>
<cell>
# Put your code here
count_uppercase_letters("Hello World!")
</cell>
<text>
Expected output: 0

</text>
<text>
Write a Python program to find the first non-repeating character in a string.

For example if the input string is "aabcccccaaa" the output should be 'c'.

You can assume the string contains at least 1 character. 
You can assume the string contains only lowercase letters. 
You can assume the string contains only alphanumeric characters. 
If the string length is longer than 1 character return None. 
If the string length is 0 return an empty string.


</text>
<cell>
def first_non_repeated_char(text):
    """
    Write a Python program to find the first non-repeating character in a string.
    """
    
    char = ''
    
    if len(text) == 0:
        return ''
    
    for letter in text:
        if letter in char:
            char = ''
        else:
            char = char + letter
            
    return char
</cell>
<cell>
# Test your code
first_non_repeated_char("aabcccccaaa")
</cell>
<text>
Expected output: 'c'

</text>
<cell>
# Put your code here
