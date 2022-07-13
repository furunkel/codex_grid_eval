
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 3, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 11, so the result would be "Plong".
    33 has both 3 and 11 as factors, but not 7, so the result would be "PlangBuzz".
    2 is not factored by 3, 11, or 7, so the result would be "2".
    """
    if num % 3 == 0:
        return "Plang"
    elif num % 11 == 0:
        return "Buzz"
    elif num % 7 == 0:
        return "Plong"
    else:
        return str(num)

# Now let's test your function
print(raindrops(14))
print(raindrops(33))
print(raindrops(2))
</cell>
<text>
Exercise 2: Write a function that takes a string and returns the number of vowels contained in the string.

</text>
<cell>
def vowels(s):
    """
    Your task is to count the number of vowels in a given string.
    
    The vowels are 'a', 'e', 'i', 'o', and 'u'.
    
    Your function should return the number of vowels in the given string.
    """
    vowel_count = 0
    for letter in s:
        if letter in 'aeiou':
            vowel_count += 1
    return vowel_count

# Now let's test your function
print(vowels('hello'))
print(vowels('hello '))
print(vowels(''))
</cell>
<text>
Exercise 3: Write a function that takes a string and returns the number of consonants contained in the string.

</text>
<cell>
def consonants(s):
    """
    Your task is to count the number of consonants in a given string.
    
    The consonants are 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'.
    
    Your function should return the number of consonants in the given string.
    """
    consonant_count = 0
    for letter in s:
        if letter in 'bcdfghjklmnpqrstvwxyz':
            consonant_count += 1
    return consonant_count

# Now let's test your function
print(consonants('hello'))
print(consonants('hello '))
print(consonants(''))
</cell>
<text>
Exercise 4: Write a function that takes a string and returns the number of words in the string that contain at least two vowels.

</text>
<cell>
def vowel_words(s):
    """
    Your task is to count the number of words in the given string that contain at least two vowels.
    
    The vowels are 'a', 'e', 'i', 'o', and 'u'.
    
    Your function should return the number of words in the given string that contain at least two vowels.
    """
    vowel_count = 0
    word_count = 0
    for letter in s:
        if letter in 'aeiou':
            vowel_count += 1
        if vowel_count >= 2:
            word_count += 1
    return word_count

# Now let's 