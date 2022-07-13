
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 9, we get 2, 4, 6, 8 and 9. The product of these multiples is 3456.
    Return the product of all the multiples of 2 or 9 below 1000.
    """    
    
    multiples = []
    for i in range(1, 1000):
        if i % 2 == 0:
            multiples.append(i)
        if i % 9 == 0:
            multiples.append(i)
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to get the product of a sequence of numbers. Next, write a function that takes in a list of numbers, and returns the product of the numbers in the list. For example, product_of_lists([4, 5, 6]) should return 720.


</text>
<cell>
def product_of_lists(lists):
    """
    Takes in a list of numbers, and returns the product of the numbers in the list.
    """
    
    product = 1
    for num in lists:
        product *= num
    return product
</cell>
<cell>
product_of_lists([4, 5, 6])
</cell>
<text>
Great! Now you know how to get the product of a list of numbers. Next, write two functions that compute their sum and product. You can base either of those off the previous functions. For example, sum([1, 2, 3]) should return 6. product_of_lists([4, 5, 6]) should return 720.


</text>
<cell>
def sum_of_lists(lists):
    """
    Takes in a list of numbers, and returns the sum of all the numbers in the list.
    """
    
    sum = 0
    for num in lists:
        sum += num
    return sum
</cell>
<cell>
sum_of_lists([4, 5, 6])
</cell>
<cell>
def product_of_lists(lists):
    """
    Takes in a list of numbers, and returns the product of all the numbers in the list.
    """
    
    product = 1
    for num in lists:
        product *= num
    return product
</cell>
<cell>
product_of_lists([4, 5, 6])
</cell>
<text>
Problem 3
The Fibonacci sequence is defined by the formula:

$Fn = \begin{cases}
0 & \text{if } n = 0\
1 & \text{if } n = 1 \
F{n-1} + F_{n-2} & \text{otherwise}
\end{cases}$

where $F_n$ is the n-th number in the Fibonacci sequence. For example, the 6th number in the sequence is $F_6 = \begin{cases}
0 & \text{if } n = 5\
1 & \text{if } n = 6\
3 & \text{if } n = 7\
5 & \text{if } n = 8\
8 & \text{if } n = 9\
\end{cases}$

Write 