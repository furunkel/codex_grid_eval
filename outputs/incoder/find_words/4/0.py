
def find_char_long(text):
    """
    Finds all words which are at least 3 characters long in a string.
    """
    
    chars = []
    
    for word in text.split():
        if len(word) >= 3:
            chars.append(word)
    
    return chars
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,.")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,.,")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,.,.")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,.,.,")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,.,.,.")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,.,.,.,")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,.,.,.,.")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,.,.,.,.,")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,.,.,.,.,.")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,.,.,.,.,.,")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,.,.,.,.,.,.,")
</cell>
<cell>
find_char_long("The quick brown fox jumps over the lazy dog.,.,.,.,.,.,.,.,")
</cell>
