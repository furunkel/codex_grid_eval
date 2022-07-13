
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of lowercase letters joined with a minus and True otherwise.
    """
    
    sequences = re.findall(r'[a-z]+[a-z\-]+', text)
    
    return len(sequences) == 1 and sequences[0] == text
</cell>
<cell>
joined_sequence('hello-world')
</cell>
<cell>
joined_sequence('hello-world-hi')
</cell>
<cell>
joined_sequence('hello-world-hi-there')
</cell>
<text>
Question 6
Write a function that returns True if the input string contains sequences of uppercase letters joined with a plus and False otherwise.


</text>
<cell>
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of uppercase letters joined with a plus and False otherwise.
    """
    
    sequences = re.findall(r'[A-Z]+[A-Z]+', text)
    
    return len(sequences) == 1 and sequences[0] == text
</cell>
<cell>
joined_sequence('hello-world')
</cell>
<cell>
joined_sequence('hello-world-hi')
</cell>
<cell>
joined_sequence('hello-world-hi-there')
</cell>
<text>
Question 7
Write a function that returns True if the input string contains sequences of uppercase letters joined with a minus and False otherwise.


</text>
<cell>
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of uppercase letters joined with a minus and False otherwise.
    """
    
    sequences = re.findall(r'[A-Z]+[A-Z\-]+', text)
    
    return len(sequences) == 1 and sequences[0] == text
</cell>
<cell>
joined_sequence('hello-world')
</cell>
<cell>
joined_sequence('hello-world-hi')
</cell>
<cell>
joined_sequence('hello-world-hi-there')
</cell>
<text>
Question 8
Write a function that returns True if the input string contains sequences of lowercase letters joined with a plus and False otherwise.


</text>
<cell>
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with a plus and False otherwise.
    """
    
    sequences = re.findall(r'[a-z]+[a-z]+', text)
    
    return len(sequences) == 1 and sequences[0] == text
</cell>
<cell>
joined_sequence('hello-world')
</cell>
<