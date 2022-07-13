
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i**2) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    8
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

    """
    
    dictionary = {}
    
    for i in range(1, n + 1):
        
        if i in dictionary:
            dictionary[i] = dictionary[i] + i**2
        else:
            dictionary[i] = i**2
            
    return dictionary
</cell>
<cell>
# Test your code
assert generate_dict(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}, "Your code should return {'1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64}"
</cell>
<text>
Write a function that takes a positive integer $n$ and an integer $k$, and returns the $k$-th term of the Fibonacci sequence. Since the terms are consecutive and ordered, you can return the term $k$ by either calling your function with $k = 1$, or just printing the $k$-th term of the sequence when $k = 1$.


</text>
<cell>
def fibonacci(n, k):
    """
    With a given positive integer $n$ and an integer $k$, return the $k$-th term of the Fibonacci sequence.
    
    Your function should return the term $k$ if $k = 1$, or the term $k + 1$ when $k = 2$ and so on. 
    
    Since the terms are consecutive and ordered, you can return the term $k$ by either calling your function with $k = 1$, or just printing the $k$-th term of the sequence when $k = 1$.
    """
    
    if k == 1:
        return n
    else:
        return fibonacci(n - 1, k - 1) + fibonacci(n - 1, k)
</cell>
<cell>
# Test your code
assert fibonacci(8, 1) == 8, "The first term of the Fibonacci sequence is 8."
assert fibonacci(8, 2) == 13, "The second term of the Fibonacci sequence is 13."
assert fibonacci(8, 3) == 21, "The third term of the Fibonacci sequence is 21."
assert fibonacci(8, 4) == 34, "The fourth term of the Fibonacci sequence is 34."
assert fibonacci(8, 5) == 51, "The fifth term of the Fibonacci sequence is 51."
assert fibonacci(8, 6) == 68, "The sixth term of the Fibonac