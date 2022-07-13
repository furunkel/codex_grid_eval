
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 1000 and "large" if n >= 2000 (and neither if 1000 <= n < 2000).
    """
    if n < 1000:
        return "mouse"
    elif n >= 2000:
        return "large"
    else:
        return "small"

# Test the above function
print(small_or_large(2000))
print(small_or_large(1000))
print(small_or_large(200))
print(small_or_large(10))
print(small_or_large(1))
</cell>
<text>
Exercise 2
Write a function that takes a string and returns the number of words in the string.


</text>
<cell>
def count_words(s):
    """
        Takes a string and returns the number of words in the string.
    """
    
    return len(s.split())
    
# Test the above function
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
print(count_word