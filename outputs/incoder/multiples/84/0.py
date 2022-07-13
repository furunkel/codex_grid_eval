
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 7 or 9, we get 5, 7 and 9. The sum of these multiples is 21.
    Return the sum of all the multiples of 5, 7 or 9 below 100.
    """    
    
    sum = 0
    for i in range(1, 101):
        if i % 5 == 0 or i % 7 == 0 or i % 9 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 7
Write a function that returns the greatest common divisor (GCD) of a and b. GCD is defined to be the largest integer that divides both a and b.

If the two integers do not divide equally, the function should return None. 


</text>
<cell>
def gcd(a, b):
    """
    Calculate the Greatest Common Divisor of a and b
    """
    
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(10, 5))
print(gcd(10, 15))
print(gcd(10, 25))
print(gcd(10, 35))
print(gcd(10, 45))
print(gcd(10, 55))
print(gcd(10, 65))
print(gcd(10, 75))
print(gcd(10, 85))
print(gcd(10, 95))
print(gcd(10, 100))
</cell>
<text>
Problem 8
Write a function that takes in two lists of strings and returns a dictionary with each word in the first list becoming a key and the number of times it occurs in the second list becoming a value. 


</text>
<cell>
def count_words(word_count, word_list):
    """
    Takes in two lists and returns a dictionary with the words in word_list as keys and the count of how many times they appear in word_count as values
    """
    
    dictionary = {}
    for word in word_list:
        if word in word_count:
            dictionary[word] = word_count.get(word)
        else:
            dictionary[word] = 1
    return dictionary

print(count_words({'and': 2, 'in': 2, 'to': 2, 'a': 2, 'the': 2, 'to': 2, 'be': 2, 'in': 2, 'a': 2, 'and': 2, 'the': 2, 'to': 2, 'be': 2, 'a': 2, 'and': 2, 'the': 2, 'to': 2, 'be': 2, 'a': 2, 'and': 2, 'the': 2, 'to': 2, 'be': 2, 'a': 2, 'and': 2, 'the': 2, 'to': 2, 'be': 2, 'a': 2, 'and': 2, 'the': 2, 'to': 2, 'be': 2, 'a': 2, 'and': 2, 'the': 2, 'to': 2, 'be': 2, 'a': 2, 'and': 2, 'the': 2, 'to': 2, 'be': 2, 'a': 2, 'and': 2, 'the': 2, 'to': 2, 'be': 2, 'a': 2, 'and': 2, 'the': 2, 'to': 2, 'be': 2, 'a': 2, 'and': 2, 'the': 2, 'to': 2, 'be': 2, 'a': 2, 'and': 2, 'the': 2, 'to': 2, 'be': 2, 'a': 2, 'and': 2, '