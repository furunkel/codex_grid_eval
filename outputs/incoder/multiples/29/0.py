
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 5, we get 2, 4, 5, 6 and 8. The product of these multiples is 1920.
    Return the product of all the multiples of 2 or 5 below 100.
    """    
    
    return sum([2**i for i in range(10) if i % 2 == 0 or i % 5 == 0])

# print multiples()
</cell>
<text>
Problem 3
The Fibonacci sequence is defined by the formula:

$Fn = \begin{cases}
1 & n = 0\
1 & n = 1 \
F{n-1} + F_{n-2} & n > 1
\end{cases}$

where $F_n$ is the n-th number in the Fibonacci sequence. For example, the 6th number in the sequence is $F_6 = 1$. Verify that $F4$ is in the Fibonacci sequence and calculate $F4$, $F5$, $F6$ and $F7$. Do not use loops.


</text>
<cell>
def fibonacci(n):
    """
    Calculate the nth number in the Fibonacci sequence
    """
    
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print fibonacci(6)
</cell>
<text>
Problem 4
Write a function that takes in a single letter, and returns the letter after being capitalized. For example, 
if the function inputs 'a', the function should return 'A'.

Do not use loops in your solution.


</text>
<cell>
def capitalize(letter):
    """
    Given a single letter, return that letter after being capitalized
    """
    
    return letter.upper()

# print capitalize('a')
</cell>
<text>
Problem 5
Write a Python function that takes in a list of words and returns the number of words in the list that have lengths that are a specific length. For example, if the list given was ["i", "like", "pie"], then the function should return 2, since there are 2 words in the list that have a length of 3.

Note You will probably need to use the count() method on a list in order to do this.


</text>
<cell>
def count_words(word_list):
    """
    Given a list of words, return the number of words in the list that have lengths that are a specific length
    """
    
    return len([word for word in word_list if len(word) == 3])

# print count_words(["i", "like", "pie"])
</cell>
<text>
Problem 6
Write a Python function that returns a new list made up of all the odd numbers in the range between 1 and 30. Do not use loops in your solution.


</text>
<cell>
def odd_numbers(start, end):
    """
    Return a new list made up of all the odd numbers in the range between start and end
    """
    