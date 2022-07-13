
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "small" if n >= 2000 (and neither if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    elif n >= 2000:
        return "small"
    else:
        return "large"

# Now we can test the function
print(small_or_large(10))
print(small_or_large(2000))
print(small_or_large(300))
</cell>
<text>
Exercise 3
Write a function that takes a string and returns the number of words in the string.


</text>
<cell>
def count_words(text):
    """
        Takes a string and returns the number of words in the string.
    """
    
    return len(text.split())
</cell>
<cell>
print(count_words("The quick brown fox jumps over the lazy dog"))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("The quick brown fox jumps over the lazy dog."))
