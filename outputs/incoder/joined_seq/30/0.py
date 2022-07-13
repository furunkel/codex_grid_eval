
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of uppercase letters joined with two underscores and True otherwise.
    """
    
    sequences = re.findall(r'[A-Z]{2,}', text)
    
    if len(sequences) > 0:
        return False
    else:
        return True
</cell>
<cell>
joined_sequence('__')
</cell>
<cell>
joined_sequence('__A')
</cell>
<cell>
joined_sequence('__AA')
</cell>
<cell>
joined_sequence('__AAA')
</cell>
<cell>
joined_sequence('__AAAA')
</cell>
<cell>
joined_sequence('__AAAAA')
</cell>
<cell>
joined_sequence('__AAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAAA')
</cell>
<cell>
joined_sequence('__AAAAAAAAAAAAAAA')
</cell