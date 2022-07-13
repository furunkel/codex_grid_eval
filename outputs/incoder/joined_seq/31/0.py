
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of lowercase letters joined with two underscores and True otherwise.
    """
    
    sequence = False
    
    for letter in text:
        if letter.isalpha() and letter != ' ':
            if letter == '_':
                sequence = True
            else:
                sequence = False
                break
    
    return sequence
</cell>
<cell>
joined_sequence('hello_world')
</cell>
<cell>
joined_sequence('hello_world!')
</cell>
<cell>
joined_sequence('hello_world!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
</cell>
<cell>
joined_sequence('hello_world!!!')
