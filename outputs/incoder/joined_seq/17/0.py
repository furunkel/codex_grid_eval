
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with two underscores and False otherwise.
    """
    
    sequences = re.findall(r'[a-z]{2}_[a-z]{2}', text)
    
    if len(sequences) > 0:
        return True
    else:
        return False
</cell>
<cell>
joined_sequence('abc_def')
</cell>
<cell>
joined_sequence('abc_defg')
</cell>
<cell>
joined_sequence('abc_defgh')
</cell>
<cell>
joined_sequence('abc_defghij')
</cell>
<cell>
joined_sequence('abc_defghijk')
</cell>
<cell>
joined_sequence('abc_defghijkl')
</cell>
<cell>
joined_sequence('abc_defghijklm')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_defghijklmn')
</cell>
<cell>
joined_sequence('abc_