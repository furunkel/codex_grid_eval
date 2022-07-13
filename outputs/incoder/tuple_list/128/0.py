
def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x:x[-1])[-11]

# Test your function
print(f([(7, 1, 9), (6, 2, 8), (5, 3, 7)]))
</cell>
<text>
Great Job!

</text>
<text>


</text>
<text>


</text>
<text>
Write a function that returns a list of numbers, such that $x_i=i^2$, for $1\leq i \leq n$. Test your function on the list below:


</text>
<cell>
def squares(n):
    """
    Write a function that returns a list of numbers, such that $x_i=i^2$, for $1\leq i \leq n$. Test your function 
    on the list below:
    """
    # initialize an empty list
    list_of_squares = []
    
    # range starts at 0 and stops before n-1
    for i in range(0, n):
        # append the squared number to the list
        list_of_squares.append(i**2)
        
    return list_of_squares

# Uncomment this to check your code
# print(squares(5))
</cell>
<text>
After your function is complete, find and print the value of the following expression:


</text>
<text>
$$(x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7 + x_8 + x_9 + x_10)^2$$


</text>
<cell>
def squares_2(list_of_squares):
    """
    Given a list of numbers, squares them one at a time, returning their sum
    """
    total = 0
    
    # for each number in the list
    for num in list_of_squares:
        # add the squared number to the total
        total += num
        
    return total

# Uncomment this to check your function
# print(squares_2([1,2,3,4]))
</cell>
<text>
After your function is complete, find and print the value of the following expression:


</text>
<text>
$$(x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7 + x_8 + x_9 + x_10)^2 + (x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7 + x_8 + x_9 + x_10)^2$$


</text>
<cell>
def squares_3(list_of_squares):
    """
    Given a list of numbers, squares them one at a time, returning their sum
    """
    total = 0
    
    # for each number in the list
    for num in list_of_squares:
        # add the squared number to the total
        total += num
        
    return total

# Uncomment this to check your function
# print(squares_3([1,2,3,