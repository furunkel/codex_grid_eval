
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 13 or 17, we get  and 13. The product of these multiples is 13.
    Return the product of all the multiples of 13 or 17 below 600.
    """    
    
    multiples = []
    for i in range(1, 600):
        if i % 13 == 0 or i % 17 == 0:
            multiples.append(i)
    return multiples

print(multiples())
</cell>
<text>
Problem 7
Write a function that returns the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.


</text>
<cell>
def sum_except_six(arr):
    """
    Takes in a list of numbers and returns the sum of all numbers except the sections starting with 6 and extending to the next 9
    """
    
    total = 0
    
    for num in arr:
        if num != 6:
            total += num
    return total

print(sum_except_six([6, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sum_except_six([6, 1, 2, 3, 4, 5, 6, 7, 8, 6, 9]))
print(sum_except_six([6, 1, 2, 3, 4, 5, 6, 7, 8, 6, 6, 9]))
</cell>
<text>
Problem 8
Write a function that returns the product of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.


</text>
<cell>
def product_except_six(arr):
    """
    Takes in a list of numbers and returns the product of all the numbers except the sections starting with 6 and extending to the next 9
    """
    
    product = 1
    
    for num in arr:
        if num != 6:
            product *= num
    return product

print(product_except_six([6, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(product_except_six([6, 1, 2, 3, 4, 5, 6, 7, 8, 6, 9]))
print(product_except_six([6, 1, 2, 3, 4, 5, 6, 7, 8, 6, 6, 9]))
</cell>
<text>
Problem 9
Write a function that checks to see if all the numbers in the array are equal, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).


</text>
<cell>
def all_except_six(arr):
    """
    Takes in a list of numbers and returns True if all the numbers in the array are equal, except the sections starting with 6 and extending to the next 9
    """
    
    total = 0
    
    for num in arr:
        if num != 6:
            total += num
    return total == arr[0]

print(all_except_six([6, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(all_except_six([6, 1, 2, 3, 4, 5, 6, 7, 8, 6, 9]))
print(all_except_six([6, 1, 2, 3, 4, 5, 6, 7, 8, 6, 6, 9]))
</cell>
<text>
Problem 10