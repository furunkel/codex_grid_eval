
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The product of these multiples is 24.
    Return the product of all the multiples of 2, 3 or 5 below 1000.
    """    
    
    multiples = []
    
    for i in range(1, 1000):
        if i % 2 == 0:
            multiples.append(i)
        if i % 3 == 0:
            multiples.append(i)
        if i % 5 == 0:
            multiples.append(i)
    
    return sum(multiples)

# print multiples()
</cell>
<text>
Great! Now you know how to get the product of a list. Let's do a few more exercises to practice your new skills.

Write a function that takes in a list of numbers and returns the product of the numbers. Call the function with the list of numbers stored in square_list.


</text>
<cell>
def product(numbers):
    """
    Takes in a list of numbers and returns the product of the numbers.
    """
    
    product = 1
    
    for i in numbers:
        product *= i
    
    return product

# print product(square_list)
</cell>
<text>
If you have done the above correctly, then you should be able to call the function with the list of numbers stored in square_list.

What happens if we call print with a list of numbers that don't have a product defined? Try it below:


</text>
<cell>
print product([1,2,3])
</cell>
<text>
What happens if we call print with a list of numbers that don't have a product defined? Try it below:


</text>
<cell>
print product([1,2,3,4,5])
</cell>
<text>
What happens if we call print with a list of numbers that don't have a product defined? Try it below:


</text>
<cell>
print product([1,2,3,4,5,6])
</cell>
<text>
What happens if we call print with a list of numbers that don't have a product defined? Try it below:


</text>
<cell>
print product([1,2,3,4,5,6,7,8,9,10])
</cell>
<text>
What happens if we call print with a list of numbers that don't have a product defined? Try it below:


</text>
<cell>
print product([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,9