
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 9, we get 2 and 4. The product of these multiples is 8.
    Return the product of all the multiples of 2 or 9 below 200.
    """    
    
    multiples = []
    
    for i in range(1, 201):
        if i % 2 == 0:
            if i % 9 == 0:
                multiples.append(i)
            else:
                multiples.append(i*9)
        else:
            multiples.append(i*2)
    
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to get the product of a list of numbers. Next, write a function that takes in a list of numbers, and returns the product of the numbers in the list that have no remainder.


</text>
<cell>
def no_remainder(list_of_numbers):
    """
    Takes in a list of numbers, and returns the product of those numbers which do not have a remainder when divided by 7. 
    """
    
    product = 1
    
    for i in list_of_numbers:
        if i % 7 == 0:
            product *= i
    
    return product
</cell>
<cell>
no_remainder([2,4,6,8,10,12,14,16,18,20])
</cell>
<text>
This works. But can you do better? If you look at the products of consecutive numbers, you'll see that if a number is a product of 7 then it is followed by another product of 7. That means we can cut the number of multiplications by half.

What about this pattern?

7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*